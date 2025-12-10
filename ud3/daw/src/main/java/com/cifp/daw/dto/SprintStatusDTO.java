package com.cifp.daw.dto;

public class SprintStatusDTO {

    private Long id;
    private String name;

    public SprintStatusDTO() {
    }
    public SprintStatusDTO(Long id, String name) {
        this.id = id;
        this.name = name;
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
}
