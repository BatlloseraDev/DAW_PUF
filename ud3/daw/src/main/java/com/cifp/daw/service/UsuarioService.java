package com.cifp.daw.service;

import com.cifp.daw.dto.UsuarioDTO;
import com.cifp.daw.repository.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UsuarioService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    public List<UsuarioDTO> obtenerUsuarios() {
        return usuarioRepository.findAll()
                .stream()
                .map(usuario -> new UsuarioDTO(usuario.getId(), usuario.getNombre(), usuario.getEmail()))
                .toList();
    }
}
