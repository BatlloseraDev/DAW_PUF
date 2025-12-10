package com.cifp.daw.repository;


import com.cifp.daw.model.Task;
import com.cifp.daw.model.TaskStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface TaskRepository extends JpaRepository<Task, Long>{

    //todas las tareas
    List<Task> findAll();

    //una tarea por su id
    Optional<Task> findById(Long id);



    //todas las tareas de un sprint
    List<Task> findBySprintId(Long sprintId);

    //todas las tareas de un programador
    List<Task> findByProgrammerId(Long programmerId);

    //todas las tareas de un estado concreto
    List<Task> findByStatus(TaskStatus status);

    void deleteById(Long id);

    @Query(value = "SELECT * FROM Task t WHERE t.status = :status", nativeQuery = true)
    List<Task> listTasksTaskStatus(@Param("status") TaskStatus status);

    //consulta nativa que busque tareas que busque por estimación de horas y horas invertidas
    @Query(value = "SELECT * FROM task WHERE estimated_hours = :estimatedHours AND spent_hours = :spentHours", nativeQuery = true)
    List<Task> listTasksByEstimatedHoursAndSpentHours(@Param("estimatedHours") Integer estimatedHours, @Param("spentHours") Integer spentHours);


    //Realizar una query nativa que reciba una lista de ids de tareas y busque mediante “IN” esa lista de tareas.
    @Query(value = "SELECT * FROM task WHERE id IN :taskIds", nativeQuery = true)
    List<Task> listTasksByTaskIds(@Param("taskIds") List<Long> taskIds);

}
