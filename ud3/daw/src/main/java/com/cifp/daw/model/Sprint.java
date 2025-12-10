package com.cifp.daw.model;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name="Sprint")
public class Sprint {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    @Column(name = "start_date")
    private LocalDate startDate;

    @Column(name = "end_date")
    private LocalDate endDate;

    @Column(length = 500)
    private String goal;

    @ManyToOne(fetch = FetchType.LAZY) // Muchos Sprints -> Un Estado
    @JoinColumn(name = "status_id", nullable = false) // Crea una columna 'status_id' que es FK
    private SprintStatus status;

    @OneToMany(
            mappedBy = "sprint",
            cascade = CascadeType.ALL,
            orphanRemoval = true,
            fetch = FetchType.LAZY
    )
    private Set<Task> tasks = new HashSet<>();

    //Constructor vacio
    public Sprint() {

    }


    public Sprint(String name, LocalDate startDate, LocalDate endDate, String goal, SprintStatus status) {
        this.name = name;
        this.startDate = startDate;
        this.endDate = endDate;
        this.goal = goal;
        this.status = status;
    }

    public Long getId() {
        return id;
    }
/* Comento esto porque no veo correcto poder cambiar la id autogenerada
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

    public LocalDate getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public LocalDate getEndDate() {
        return endDate;
    }

    public void setEndDate(LocalDate endDate) {
        this.endDate = endDate;
    }

    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }

    public SprintStatus getStatus() {
        return status;
    }

    public void setStatus(SprintStatus status) {
        this.status = status;
    }
    public void addTask(Task task) {
        this.tasks.add(task);
        task.setSprint(this);
    }

    public void removeTask(Task task) {
        this.tasks.remove(task);
        task.setSprint(null);
    }
}
