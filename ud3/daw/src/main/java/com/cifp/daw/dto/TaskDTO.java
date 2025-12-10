package com.cifp.daw.dto;

import com.cifp.daw.model.TaskPriority;
import com.cifp.daw.model.TaskStatus;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

public class TaskDTO {
    private Long id;
    private String title;
    private String description;
    private Integer storyPoints;
    private TaskPriorityDTO priority; // Ya no es Enum
    private TaskStatusDTO status;
    private Integer estimatedHours;
    private Integer spentHours;

    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    private Long sprintId;
    private Long programmerId;

    private Set<TagDTO> tags = new HashSet<>();
    public TaskDTO() {
    }

    public TaskDTO(Long id, String title, String description, Integer storyPoints, TaskPriorityDTO priority, TaskStatusDTO status, Integer estimatedHours, Integer spentHours, LocalDateTime createdAt, LocalDateTime updatedAt, Long sprintId, Long programmerId, Set<TagDTO> tags) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.storyPoints = storyPoints;
        this.priority = priority;
        this.status = status;
        this.estimatedHours = estimatedHours;
        this.spentHours = spentHours;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
        this.sprintId = sprintId;
        this.programmerId = programmerId;
        this.tags = tags;
    }

    // Getters y Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public Integer getStoryPoints() { return storyPoints; }
    public void setStoryPoints(Integer storyPoints) { this.storyPoints = storyPoints; }

    public TaskPriorityDTO getPriority() { return priority; }
    public void setPriority(TaskPriorityDTO priority) { this.priority = priority; }

    public TaskStatusDTO getStatus() { return status; }
    public void setStatus(TaskStatusDTO status) { this.status = status; }

    public Integer getEstimatedHours() { return estimatedHours; }
    public void setEstimatedHours(Integer estimatedHours) { this.estimatedHours = estimatedHours; }

    public Integer getSpentHours() { return spentHours; }
    public void setSpentHours(Integer spentHours) { this.spentHours = spentHours; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }

    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }

    public Long getSprintId() { return sprintId; }
    public void setSprintId(Long sprintId) { this.sprintId = sprintId; }

    public Long getProgrammerId() { return programmerId; }
    public void setProgrammerId(Long programmerId) { this.programmerId = programmerId; }

    public Set<TagDTO> getTags() { return tags; }
    public void setTags(Set<TagDTO> tags) { this.tags = tags; }
}
