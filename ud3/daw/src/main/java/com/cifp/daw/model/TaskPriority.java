package com.cifp.daw.model;

import jakarta.persistence.*;

@Entity
@Table(name = "task_priority")
public class TaskPriority {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true) // Ej: HIGH, LOW...
    private String name;

    public TaskPriority() {
    }

    public TaskPriority(String name) {
        this.name = name;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}