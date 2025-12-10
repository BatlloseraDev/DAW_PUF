package com.cifp.daw.repository;

import com.cifp.daw.model.Tag;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface TagRepository extends JpaRepository<Tag, Long> {

    //para buscar si existe ya una etiqueta antes de crearla
    Optional<Tag> findByName(String name);

}
