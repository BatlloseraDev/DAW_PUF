package com.cifp.daw.dto;

import com.cifp.daw.model.RolProgrammer;


public class ProgrammerDTO {
    private Long id;
    private String name;
    private String email;
    private RolProgrammer rol;
    private Integer capacity;

    public ProgrammerDTO() {
    }
    public ProgrammerDTO(Long id,String name, String email, RolProgrammer rol, Integer capacity) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.rol = rol;
        this.capacity = capacity;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public RolProgrammer getRol() {
        return rol;
    }

    public void setRol(RolProgrammer rol) {
        this.rol = rol;
    }

    public Integer getCapacity() {
        return capacity;
    }

    public void setCapacity(Integer capacity) {
        this.capacity = capacity;
    }
}
