package com.cifp.daw.model;


import jakarta.persistence.*;

@Entity
public class Programmer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    @Column(unique = true)
    private String email;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "rol_id", nullable = false)
    private RolProgrammer rol;


    private Integer capacity;

    public Programmer() {
    }
    public Programmer(String name, String email, RolProgrammer rol, Integer capacity) {
        this.name = name;
        this.email = email;
        this.rol = rol;
        this.capacity = capacity;
    }

    public Long getId() {
        return id;
    }
/*
    public void setId(Long id) {
        this.id = id;
    }
*/
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
