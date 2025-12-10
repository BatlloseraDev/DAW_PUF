package com.cifp.daw.controller;

import com.cifp.daw.dto.ProgrammerDTO;
import com.cifp.daw.model.RolProgrammer;
import com.cifp.daw.service.ProgrammerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/programmers")
public class ProgrammerController {

    private final ProgrammerService programmerService;

    @Autowired
    public ProgrammerController(ProgrammerService programmerService) {
        this.programmerService = programmerService;
    }

    //todos los programadores
    @GetMapping
    public ResponseEntity<List<ProgrammerDTO>> getAllProgrammers() {
        return ResponseEntity.ok(programmerService.getAllProgrammers());
    }

    //por id
    @GetMapping("/{id}")
    public ResponseEntity<ProgrammerDTO> getProgrammerById(@PathVariable Long id){
        ProgrammerDTO programmer = programmerService.getProgrammerById(id);
        if (programmer != null) {
            return ResponseEntity.ok(programmer);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    //Crear programador
    @PostMapping
    public ResponseEntity<ProgrammerDTO> createProgrammer(@RequestBody ProgrammerDTO programmerDTO) {
        try{
            ProgrammerDTO createdProgrammer = programmerService.createProgrammer(programmerDTO);
            return new ResponseEntity<>(createdProgrammer, HttpStatus.CREATED);
        }catch (IllegalArgumentException e){
            return ResponseEntity.badRequest().body(null);
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteProgrammer(@PathVariable Long id) {
        programmerService.deleteProgrammer(id);
        return ResponseEntity.noContent().build();
    }

    //filtrar por rol
    @GetMapping("/rol/{rolName}")
    public ResponseEntity<List<ProgrammerDTO>> getByRol(@PathVariable String rolName) {
        return ResponseEntity.ok(programmerService.getProgrammersByRol(rolName));
    }

    //filtrar por rol y capacidad
    @GetMapping("/search") //por ejemplo: GET http://localhost:8080/programmers/search?rol=DEV&capacity=20
    public ResponseEntity<List<ProgrammerDTO>> getByRolAndCapacity(
            @RequestParam String rol, // Spring leerá "DEV" como String
            @RequestParam Integer capacity) {

        List<ProgrammerDTO> programmers = programmerService.getProgrammersByRolAndCapacity(rol, capacity);
        return ResponseEntity.ok(programmers);
    }

    @PutMapping("/{id}")
    public ResponseEntity<ProgrammerDTO> updateProgrammer(@PathVariable Long id, @RequestBody ProgrammerDTO programmerDTO) {
        ProgrammerDTO updated = programmerService.updateProgrammer(id, programmerDTO);
        if (updated != null) {
            return ResponseEntity.ok(updated);
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
