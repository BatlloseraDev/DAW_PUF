package com.cifp.daw.repository;

import com.cifp.daw.model.TaskPriority;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface TaskPriorityRepository extends JpaRepository<TaskPriority, Long> {
    Optional<TaskPriority> findByName(String name);
}

/*
*
* NSERT INTO task_status (name) VALUES ('TODO'), ('DOING'), ('REVIEW'), ('DONE');
INSERT INTO task_priority (name) VALUES ('LOW'), ('MEDIUM'), ('HIGH'), ('CRITICAL');
* */