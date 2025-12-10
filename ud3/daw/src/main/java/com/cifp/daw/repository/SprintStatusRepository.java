package com.cifp.daw.repository;

import com.cifp.daw.model.SprintStatus;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;


public interface SprintStatusRepository extends JpaRepository<SprintStatus, Long> {

    Optional<SprintStatus> findByName(String name);
}
