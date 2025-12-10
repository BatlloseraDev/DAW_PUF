package com.cifp.daw.model;

import jakarta.persistence.*;

@Entity
@Table(name = "rol_programmer")
public class RolProgrammer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true) // 'DEV', 'TEST', 'LEAD' no pueden repetirse
    private String name;

    public RolProgrammer() {
    }

    public RolProgrammer(String name) {
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