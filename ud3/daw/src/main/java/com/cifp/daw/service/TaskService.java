package com.cifp.daw.service;


import com.cifp.daw.dto.TagDTO;
import com.cifp.daw.dto.TaskDTO;
import com.cifp.daw.dto.TaskPriorityDTO;
import com.cifp.daw.dto.TaskStatusDTO;
import com.cifp.daw.model.*;
import com.cifp.daw.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

@Service
public class TaskService {

    private final TaskRepository taskRepository;
    private final SprintRepository sprintRepository;
    private final ProgrammerRepository programmerRepository;
    private final TagRepository tagRepository;

    private final TaskStatusRepository taskStatusRepository;
    private final TaskPriorityRepository taskPriorityRepository;

    @Autowired
    public TaskService(TaskRepository taskRepository,
                       SprintRepository sprintRepository,
                       ProgrammerRepository programmerRepository,
                       TagRepository tagRepository,
                       TaskStatusRepository taskStatusRepository,
                       TaskPriorityRepository taskPriorityRepository) {
        this.taskRepository = taskRepository;
        this.sprintRepository = sprintRepository;
        this.programmerRepository = programmerRepository;
        this.tagRepository = tagRepository;
        this.taskStatusRepository = taskStatusRepository;
        this.taskPriorityRepository = taskPriorityRepository;
    }

    //obtener todas las tareas
    public List<TaskDTO> getAllTasks(){
        return taskRepository.findAll().stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());
    }

    //obtener una tarea por su id
    public Optional<TaskDTO> getTaskById(Long id){
        return taskRepository.findById(id).map(this::mapToDTO);
    }

    //obtener todas las tareas de un sprint
    public List<TaskDTO> getTasksBySprintId(Long sprintId){
        return taskRepository.findBySprintId(sprintId).stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());

    }
    //obtener todas las tareas de un programador
    public List<TaskDTO> getTasksByProgrammer(Long programmerId){
        return taskRepository.findByProgrammerId(programmerId).stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());
    }

    //Crear tarea
    @Transactional //para que si algo falle no se guarde nada
    public TaskDTO createTask(TaskDTO taskDTO) {
        if(taskDTO.getStoryPoints() !=null){
            if(taskDTO.getStoryPoints() < 0 || taskDTO.getStoryPoints() > 100){
                throw new IllegalArgumentException("Los puntos de historia deben estar entre 0 y 100");
            }
        }

        Sprint sprint = sprintRepository.findById(taskDTO.getSprintId())
                .orElseThrow(()-> new IllegalArgumentException("Sprint no encontrado"));

        Programmer programmer = programmerRepository.findById(taskDTO.getProgrammerId())
                .orElseThrow(()-> new IllegalArgumentException("Programador no encontrado"));

        Task task = new Task();
        task.setTitle(taskDTO.getTitle());
        task.setDescription(taskDTO.getDescription());
        task.setStoryPoints(taskDTO.getStoryPoints());
        task.setEstimatedHours(taskDTO.getEstimatedHours());
        task.setSpentHours(taskDTO.getSpentHours());

        //  LÓGICA PARA ASIGNAR PRIORIDAD
        if (taskDTO.getPriority() != null && taskDTO.getPriority().getName() != null) {
            TaskPriority priority = taskPriorityRepository.findByName(taskDTO.getPriority().getName())
                    .orElseThrow(() -> new IllegalArgumentException("Prioridad no válida"));
            task.setPriority(priority);
        } else {
            //  Asignar prioridad por defecto (ej. MEDIUM) si no viene nada
            task.setPriority(taskPriorityRepository.findByName("MEDIUM").orElse(null));
        }

        if (taskDTO.getStatus() != null && taskDTO.getStatus().getName() != null) {
            TaskStatus status = taskStatusRepository.findByName(taskDTO.getStatus().getName())
                    .orElseThrow(() -> new IllegalArgumentException("Estado no válido"));
            task.setStatus(status);
        } else {
            // Lógica por defecto: Si no trae estado, asignamos "TODO"
            TaskStatus defaultStatus = taskStatusRepository.findByName("TODO")
                    .orElseThrow(() -> new RuntimeException("El estado 'TODO' no existe en la BD."));
            task.setStatus(defaultStatus);
        }

        task.setSprint(sprint);
        task.setProgrammer(programmer);

        Set<Tag> tagsToSave = processTags(taskDTO.getTags());
        task.setTags(tagsToSave);

        Task savedTask = taskRepository.save(task);
        return mapToDTO(savedTask);
    }

    //actualizar una tarea
    @Transactional
    public TaskDTO updateTask(Long id, TaskDTO taskDTO){
        Task task = taskRepository.findById(id)
                .orElseThrow(()-> new IllegalArgumentException("Tarea no encontrada"));

        if(taskDTO.getStoryPoints() !=null && (taskDTO.getStoryPoints() < 0 || taskDTO.getStoryPoints() > 100)){
            throw new IllegalArgumentException("Los puntos de historia deben estar entre 0 y 100");
        }

        if(taskDTO.getSprintId() != null){
            Sprint newSprint = sprintRepository.findById(taskDTO.getSprintId())
                    .orElseThrow(()-> new IllegalArgumentException("Sprint no encontrado"));
            task.setSprint(newSprint);
        }

        if(taskDTO.getProgrammerId() != null){
            Programmer programmer = programmerRepository.findById(taskDTO.getProgrammerId())
                    .orElseThrow(()-> new IllegalArgumentException("Programador no encontrado"));
            task.setProgrammer(programmer);
        }

        task.setTitle(taskDTO.getTitle());
        task.setDescription(taskDTO.getDescription());
        task.setStoryPoints(taskDTO.getStoryPoints());
        task.setEstimatedHours(taskDTO.getEstimatedHours());
        task.setSpentHours(taskDTO.getSpentHours());

        // 4. ACTUALIZAR PRIORIDAD (Solo si viene en el DTO)
        if (taskDTO.getPriority() != null && taskDTO.getPriority().getName() != null) {
            TaskPriority priority = taskPriorityRepository.findByName(taskDTO.getPriority().getName())
                    .orElseThrow(() -> new IllegalArgumentException("Prioridad no encontrada"));
            task.setPriority(priority);
        }

        // 5. ACTUALIZAR ESTADO (Solo si viene en el DTO)
        if (taskDTO.getStatus() != null && taskDTO.getStatus().getName() != null) {
            TaskStatus status = taskStatusRepository.findByName(taskDTO.getStatus().getName())
                    .orElseThrow(() -> new IllegalArgumentException("Estado no encontrado"));
            task.setStatus(status);
        }

        Set<Tag> updatedTags = processTags(taskDTO.getTags());
        task.setTags(updatedTags);

        Task updatedTask = taskRepository.save(task);
        return mapToDTO(updatedTask);
    }

    //borrar la tarea
    public void deleteTask(Long id) {
        taskRepository.deleteById(id);
    }



    //metodos auxiliares
    private TaskDTO mapToDTO(Task task) {
        TaskDTO dto = new TaskDTO();
        dto.setId(task.getId());
        dto.setTitle(task.getTitle());
        dto.setDescription(task.getDescription());
        dto.setStoryPoints(task.getStoryPoints());
        dto.setEstimatedHours(task.getEstimatedHours());
        dto.setSpentHours(task.getSpentHours());
        dto.setCreatedAt(task.getCreatedAt());
        dto.setUpdatedAt(task.getUpdatedAt());

        // MAPEO DE ENTIDAD A DTO (Prioridad)
        if (task.getPriority() != null) {
            TaskPriorityDTO priorityDTO = new TaskPriorityDTO();
            priorityDTO.setId(task.getPriority().getId());
            priorityDTO.setName(task.getPriority().getName());
            dto.setPriority(priorityDTO);
        }

        //. MAPEO DE ENTIDAD A DTO (Estado)
        if (task.getStatus() != null) {
            TaskStatusDTO statusDTO = new TaskStatusDTO();
            statusDTO.setId(task.getStatus().getId());
            statusDTO.setName(task.getStatus().getName());
            dto.setStatus(statusDTO);
        }

        if (task.getSprint() != null) {
            dto.setSprintId(task.getSprint().getId());
        }
        if (task.getProgrammer() != null) {
            dto.setProgrammerId(task.getProgrammer().getId());
        }

        Set<TagDTO> tagDTOs = task.getTags().stream()
                .map(tag -> new TagDTO(tag.getId(), tag.getName()))
                .collect(Collectors.toSet());
        dto.setTags(tagDTOs);

        return dto;
    }

    private Set<Tag> processTags(Set<TagDTO> tagDTOs) {
        Set<Tag> tags = new HashSet<>();
        if (tagDTOs != null) {
            for (TagDTO tagDTO : tagDTOs) {
                // Busco si ya existe una etiqueta con ese nombre
                // Usa el repositorio de Tag
                Optional<Tag> existingTag = tagRepository.findByName(tagDTO.getName());

                if (existingTag.isPresent()) {
                    // Si existe, la reutilizo
                    tags.add(existingTag.get());
                } else {
                    // Si no existe, creo una nueva y la guardo en BD
                    Tag newTag = new Tag(tagDTO.getName());
                    tags.add(tagRepository.save(newTag));
                }
            }
        }
        return tags;
    }

}
