package com.cifp.daw.repository;

import com.cifp.daw.model.Programmer;
import com.cifp.daw.model.RolProgrammer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ProgrammerRepository extends JpaRepository<Programmer, Long> {

    Optional<Programmer> findByEmail(String email);
    List<Programmer> findByRol(RolProgrammer rol);
    boolean existsByEmail(String email);
    List<Programmer> findByRolAndCapacityGreaterThan(RolProgrammer rol, Integer capacity);

}
