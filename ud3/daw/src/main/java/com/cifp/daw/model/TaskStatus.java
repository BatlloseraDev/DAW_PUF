package com.cifp.daw.model;

import jakarta.persistence.*;

@Entity
@Table(name = "task_status")
public class TaskStatus {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true) // Ej: TODO, DOING...
    private String name;

    public TaskStatus() {
    }

    public TaskStatus(String name) {
        this.name = name;
    }

    public Long getId() {
        return id;
    }

    // No ponemos setId manual si es autogenerado

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}