package com.cifp.daw.controller;

import com.cifp.daw.dto.TaskDTO;
import com.cifp.daw.service.TaskService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/tasks")
public class TaskController {

    private final TaskService taskService;

    @Autowired
    public TaskController(TaskService taskService) {
        this.taskService = taskService;
    }

    //Obtener todas las tareas
    @GetMapping
    public ResponseEntity<List<TaskDTO>> getAllTasks() {
        return ResponseEntity.ok(taskService.getAllTasks());
    }

    //Obtener tarea por ID
    @GetMapping("/{id}")
    public ResponseEntity<TaskDTO> getTaskById(@PathVariable Long id) {
        return taskService.getTaskById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    //Crear nueva tarea
    @PostMapping
    public ResponseEntity<?> createTask(@RequestBody TaskDTO taskDTO) {
        try {
            TaskDTO createdTask = taskService.createTask(taskDTO);
            return new ResponseEntity<>(createdTask, HttpStatus.CREATED);
        } catch (IllegalArgumentException e) {
            // Capturamos errores de validación (Story points inválidos, Sprint no existe, etc.)
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    //Actualizar tarea
    @PutMapping("/{id}")
    public ResponseEntity<?> updateTask(@PathVariable Long id, @RequestBody TaskDTO taskDTO) {
        try {
            TaskDTO updatedTask = taskService.updateTask(id, taskDTO);
            return ResponseEntity.ok(updatedTask);
        } catch (IllegalArgumentException e) {
            // Si el ID no existe o los datos son inválidos
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    //Borrar tarea
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteTask(@PathVariable Long id) {
        taskService.deleteTask(id);
        return ResponseEntity.noContent().build();
    }


    //Obtener tareas de un Sprint concreto
    // Ejemplo: GET http://localhost:8080/tasks/sprint/5
    @GetMapping("/sprint/{sprintId}")
    public ResponseEntity<List<TaskDTO>> getTasksBySprint(@PathVariable Long sprintId) {
        List<TaskDTO> tasks = taskService.getTasksBySprintId(sprintId);
        return ResponseEntity.ok(tasks);
    }

    // Obtener tareas de un Programador concreto
    //Ejemplo:  GET http://localhost:8080/tasks/programmer/2
    @GetMapping("/programmer/{programmerId}")
    public ResponseEntity<List<TaskDTO>> getTasksByProgrammer(@PathVariable Long programmerId) {
        List<TaskDTO> tasks = taskService.getTasksByProgrammer(programmerId);
        return ResponseEntity.ok(tasks);
    }

}
