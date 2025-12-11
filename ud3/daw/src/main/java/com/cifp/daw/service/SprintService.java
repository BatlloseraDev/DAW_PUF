package com.cifp.daw.service;



import com.cifp.daw.dto.SprintDTO;
import com.cifp.daw.dto.SprintStatusDTO;
import com.cifp.daw.model.Sprint;
import com.cifp.daw.model.SprintStatus;
import com.cifp.daw.repository.SprintRepository;
import com.cifp.daw.repository.SprintStatusRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors; // Ayuda a parametrizar

@Service
public class SprintService {

    @Autowired
    private SprintRepository sprintRepository;

    @Autowired
    private SprintStatusRepository sprintStatusRepository;

    //conseguir todos
    public List<SprintDTO> getAllSprints() {
        List<Sprint> sprints = sprintRepository.findAll();
        return sprints.stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());
    }
    //conseguir por id
    public SprintDTO getSprintById(Long id) {
        Sprint sprint = sprintRepository.findById(id).orElse(null);
        if(sprint==null)
            return null;
        else
            return mapToDTO(sprint);

    }

    //conseguir por estado
    public List<SprintDTO> getSprintByStatus(SprintStatus status){
        List<Sprint> sprints = sprintRepository.findByStatus(status);
        if(sprints.isEmpty())
            return null;
        else
            return sprints.stream()
                    .map(this::mapToDTO)
                    .collect(Collectors.toList());

    }

    // crear Srpint (recibe dto guarda entidad y devuelve el dto)
    public SprintDTO createSprint(SprintDTO sprintDTO) {
        //Primero valido
        if(sprintDTO.getStartDate() != null && sprintDTO.getEndDate() != null){
            if(sprintDTO.getStartDate().isAfter(sprintDTO.getEndDate())){
                throw new IllegalArgumentException("La fecha fin  no puede ser anterior a la fecha inicio");
            }
        }
        Sprint sprint = new Sprint();
        //Aqui no añado el id
        sprint.setName(sprintDTO.getName());
        sprint.setStartDate(sprintDTO.getStartDate());
        sprint.setEndDate(sprintDTO.getEndDate());
        sprint.setGoal(sprintDTO.getGoal());

        SprintStatus statusEntity;

        if(sprintDTO.getStatus() != null && sprintDTO.getStatus().getId() != null){
            String statusName = sprintDTO.getStatus().getName();
            statusEntity = sprintStatusRepository.findByName(statusName)
                    .orElseThrow(()-> new RuntimeException("El estado enviado no existe en la base de datos"));
        }
        else {
            statusEntity = sprintStatusRepository.findByName("PLANNED")
                    .orElse(null);
        }

        sprint.setStatus(statusEntity);


        Sprint savedSprint = sprintRepository.save(sprint);

        return mapToDTO(savedSprint);
    }

    //actualizar un sprint existente
    public SprintDTO updateSprint(Long id, SprintDTO sprintDTO) {
        //libreria que me permite controlar si existe o no
        Optional<Sprint> optionalSprint = sprintRepository.findById(id);

        if(optionalSprint.isPresent()){
            Sprint sprint = optionalSprint.get();

            sprint.setName(sprintDTO.getName());
            sprint.setStartDate(sprintDTO.getStartDate());
            sprint.setEndDate(sprintDTO.getEndDate());
            sprint.setGoal(sprintDTO.getGoal());

            if(sprintDTO.getStatus() != null){
                SprintStatus status= sprintStatusRepository.findByName(sprintDTO.getStatus().getName())
                        .orElseThrow(()-> new RuntimeException("El estado enviado no existe en la base de datos"));
                sprint.setStatus(status);
            }

            Sprint updatedSprint = sprintRepository.save(sprint);
            return mapToDTO(updatedSprint);
        }else{
            return null;// también podría lanzar un error
        }
    }

    //eliminar un sprint
    public void deleteSprint(Long id) {
        sprintRepository.deleteById(id);
    }
    // ACTIVIDAD 4: Buscar Sprints por texto en el objetivo (goal) y lista de IDs
    public List<SprintDTO> searchSprintsByGoalAndIds(String goal, List<Long> ids) {
        List<Sprint> sprints = sprintRepository.findByGoalContainingAndIdIn(goal, ids);


        return sprints.stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());
    }



    //Mapeadores asi no pongo tanto codigo redundante

    private SprintDTO mapToDTO(Sprint sprint) {
        SprintDTO dto = new SprintDTO();
        dto.setId(sprint.getId());
        dto.setName(sprint.getName());
        dto.setStartDate(sprint.getStartDate());
        dto.setEndDate(sprint.getEndDate());
        dto.setGoal(sprint.getGoal());
        if (sprint.getStatus() != null) {
            SprintStatusDTO statusDTO = new SprintStatusDTO(
                    sprint.getStatus().getId(),
                    sprint.getStatus().getName()
            );
            dto.setStatus(statusDTO);
        }

        return dto;
    }


}
