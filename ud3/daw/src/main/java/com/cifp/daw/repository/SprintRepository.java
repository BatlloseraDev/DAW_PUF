package com.cifp.daw.repository;

import com.cifp.daw.model.Sprint;
import com.cifp.daw.model.SprintStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface SprintRepository extends JpaRepository<Sprint, Long> {
    //Buscar sprints por su nombre, en este caso es como el LIKE
    List<Sprint> findByNameContaining(String name);

    //Buscar sprints por su estado
    List<Sprint> findByStatus(SprintStatus status);

    //Actividad 4 Realizar una consulta nativa que busque por objetivo y lista de sprints.
    @Query(value = "SELECT * FROM sprint WHERE goal LIKE '%' || :goal || '%' AND id IN :ids", nativeQuery = true)
    List<Sprint> findByGoalContainingAndIdIn(@Param("goal") String goal, @Param("ids") List<Long> ids);

}
