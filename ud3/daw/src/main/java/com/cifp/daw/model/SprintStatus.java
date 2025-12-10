package com.cifp.daw.model;

import jakarta.persistence.*;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Entity
@Table(name = "sprint_status")
public class SprintStatus {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true) // El nombre no puede ser nulo y no debe repetirse
    private String name;


    @OneToMany(
            mappedBy = "status",
            cascade = CascadeType.ALL,
            orphanRemoval = true,
            fetch = FetchType.LAZY
    )
    private Set<Sprint> sprints = new HashSet<>();

    public SprintStatus() {
    }

    public SprintStatus(String name) {
        this.name = name;
    }

    // Getters y Setters
    public Long getId() {
        return id;
    }

    // Mantenemos tu filosofía de no exponer el setId si es autogenerado

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}