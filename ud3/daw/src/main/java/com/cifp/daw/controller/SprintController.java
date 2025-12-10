package com.cifp.daw.controller;

import com.cifp.daw.dto.SprintDTO;
import com.cifp.daw.model.SprintStatus;
import com.cifp.daw.service.SprintService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/sprints")
public class SprintController {

    private final SprintService sprintService;

    @Autowired
    public SprintController(SprintService sprintService) {
        this.sprintService = sprintService;
    }

    //Obtener todos los sprints
    @GetMapping
    public ResponseEntity<List<SprintDTO>> getAllSprints() {
        List<SprintDTO> sprints = sprintService.getAllSprints();
        return ResponseEntity.ok(sprints);
    }

    //Obtener un sprint por su ID
    @GetMapping("/{id}")
    public ResponseEntity<SprintDTO> getSprintById(@PathVariable Long id) {
        SprintDTO sprint = sprintService.getSprintById(id);
        if (sprint != null) {
            return ResponseEntity.ok(sprint);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    //Obtener Srpint por estado
    @GetMapping("/status/{status}")
    public ResponseEntity<List<SprintDTO>> getSprintByStatus(@PathVariable SprintStatus status) {
        List<SprintDTO> sprints = sprintService.getSprintByStatus(status);
        if (sprints != null) {
            return ResponseEntity.ok(sprints);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    //Crear un nuevo sprint
    @PostMapping
    public ResponseEntity<SprintDTO> createSprint(@RequestBody SprintDTO sprintDTO) {
        SprintDTO sprint = sprintService.createSprint(sprintDTO);
        return new ResponseEntity<>(sprint, HttpStatus.CREATED);
    }

    //Actualizar un sprint existente
    @PutMapping("/{id}")
    public ResponseEntity<SprintDTO> updateSprint(@RequestBody SprintDTO sprintDTO, @PathVariable Long id) {
        SprintDTO sprint = sprintService.updateSprint(id, sprintDTO);
        if (sprint != null) {
            return ResponseEntity.ok(sprint);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    //Eliminar un sprint
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteSprint(@PathVariable Long id) {
        sprintService.deleteSprint(id);
        return ResponseEntity.noContent().build();
    }
}
