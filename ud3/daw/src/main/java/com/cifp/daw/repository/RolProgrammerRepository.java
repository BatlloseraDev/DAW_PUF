package com.cifp.daw.repository;

import com.cifp.daw.model.RolProgrammer;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface RolProgrammerRepository extends JpaRepository<RolProgrammer, Long> {
    Optional<RolProgrammer> findByName(String name);
}

/*
*
* INSERT INTO rol_programmer (name) VALUES ('DEV');
INSERT INTO rol_programmer (name) VALUES ('TEST');
INSERT INTO rol_programmer (name) VALUES ('LEAD');
*
* */
