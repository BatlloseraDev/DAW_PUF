package com.cifp.daw.dto;

import com.cifp.daw.model.SprintStatus;

import java.time.LocalDate;

public class SprintDTO {

    private Long id;
    private String name;
    private LocalDate startDate;
    private LocalDate endDate;
    private String goal;
    private SprintStatusDTO status;

    public SprintDTO() {}
    public SprintDTO(Long id, String name, LocalDate startDate, LocalDate endDate, String goal, SprintStatusDTO status) {
        this.id = id;
        this.name = name;
        this.startDate = startDate;
        this.endDate = endDate;
        this.goal = goal;
        this.status = status;
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

    public SprintStatusDTO getStatus() {
        return status;
    }

    public void setStatus(SprintStatusDTO status) {
        this.status = status;
    }
}
