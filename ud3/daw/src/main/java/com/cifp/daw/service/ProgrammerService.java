package com.cifp.daw.service;


import com.cifp.daw.dto.ProgrammerDTO;
import com.cifp.daw.model.Programmer;
import com.cifp.daw.model.RolProgrammer;
import com.cifp.daw.repository.ProgrammerRepository;
import com.cifp.daw.repository.RolProgrammerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class ProgrammerService {
    @Autowired
    private ProgrammerRepository programmerRepository;

    @Autowired
    private RolProgrammerRepository rolProgrammerRepository;

    //obtiene a todos los programadores
    public List<ProgrammerDTO> getAllProgrammers() {
        List<Programmer> programmers = programmerRepository.findAll();
        return programmers.stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());
    }

    //programador por id
    public ProgrammerDTO getProgrammerById(Long id) {
        Programmer programmer = programmerRepository.findById(id).orElse(null);
        if (programmer == null) {
            return null;
        } else {
            return mapToDTO(programmer);
        }
    }
    //programador por rol --------->cambiar
    public List<ProgrammerDTO> getProgrammersByRol(String rolName) {

        RolProgrammer rolEntity = rolProgrammerRepository.findByName(rolName)
                .orElse(null);

        if(rolEntity == null) return List.of(); //controla que tengan un rol
        //Si la ha encontrado la devuelve
        List<Programmer> programmers = programmerRepository.findByRol(rolEntity);


        return programmers.stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());
    }

    public List<ProgrammerDTO> getProgrammersByRolAndCapacity(String rolName, Integer capacity) {

        RolProgrammer rolEntity = rolProgrammerRepository.findByName(rolName)
                .orElse(null);

        if (rolEntity == null) return List.of();

        List<Programmer> programmers = programmerRepository.findByRolAndCapacityGreaterThan(rolEntity, capacity);

        return programmers.stream()
                .map(this::mapToDTO)
                .collect(Collectors.toList());
    }


    //crear programador
    public ProgrammerDTO createProgrammer(ProgrammerDTO programmerDTO) {
        if (programmerRepository.existsByEmail(programmerDTO.getEmail())) {
            throw new IllegalArgumentException("Ya existe un programador con este email.");
        }

        Programmer programmer = new Programmer();
        programmer.setName(programmerDTO.getName());
        programmer.setEmail(programmerDTO.getEmail());
        programmer.setCapacity(programmerDTO.getCapacity());

        if (programmerDTO.getRol() != null && programmerDTO.getRol().getName() != null) {
            RolProgrammer rol = rolProgrammerRepository.findByName(programmerDTO.getRol().getName())
                    .orElseThrow(() -> new IllegalArgumentException("El rol especificado no existe: " + programmerDTO.getRol().getName()));
            programmer.setRol(rol);
        } else {
            throw new IllegalArgumentException("El rol es obligatorio.");
        }


        Programmer savedProgrammer = programmerRepository.save(programmer);
        return mapToDTO(savedProgrammer);
    }

    //actualizar programador
    public ProgrammerDTO updateProgrammer(Long id, ProgrammerDTO programmerDTO) {
        Optional<Programmer> optionalProgrammer = programmerRepository.findById(id);

        if (optionalProgrammer.isPresent()) {
            Programmer programmer = optionalProgrammer.get();

            //Validar email único (excluyendo el propio usuario)
            if (!programmer.getEmail().equals(programmerDTO.getEmail()) && programmerRepository.existsByEmail(programmerDTO.getEmail())) {
                throw new IllegalArgumentException("Ya existe otro programador con este email.");
            }

            programmer.setName(programmerDTO.getName());
            programmer.setEmail(programmerDTO.getEmail());
            programmer.setCapacity(programmerDTO.getCapacity());

            if (programmerDTO.getRol() != null) {
                RolProgrammer rol = rolProgrammerRepository.findByName(programmerDTO.getRol().getName())
                        .orElseThrow(() -> new IllegalArgumentException("El rol especificado no existe."));
                programmer.setRol(rol);
            }


            Programmer updatedProgrammer = programmerRepository.save(programmer);
            return mapToDTO(updatedProgrammer);
        } else {
            return null;
        }
    }

    //eliminar programador
    public void deleteProgrammer(Long id) {
        programmerRepository.deleteById(id);
    }



    private ProgrammerDTO mapToDTO(Programmer programmer) {
        ProgrammerDTO dto = new ProgrammerDTO();
        dto.setId(programmer.getId());
        dto.setName(programmer.getName());
        dto.setEmail(programmer.getEmail());
        dto.setRol(programmer.getRol());//Si no lo recibe como un json reventará
        dto.setCapacity(programmer.getCapacity());
        return dto;
    }



}
