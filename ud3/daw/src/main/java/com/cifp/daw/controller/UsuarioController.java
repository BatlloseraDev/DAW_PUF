package com.cifp.daw.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UsuarioController {
    @GetMapping("/api/hello")
    public String hola() {
        return "Hola";
    }

    @GetMapping("/api/adios")
    public String home() {
        return "Adios";
    }
}