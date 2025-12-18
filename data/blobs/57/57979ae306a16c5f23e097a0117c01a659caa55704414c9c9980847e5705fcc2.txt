package com.generation.hello_world.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Arrays;

@RestController
@RequestMapping("/api")
public class HelloWorldController {

    @GetMapping("/hello-world")
    public String helloWorld() {
        return "Hello World!";
    }

    @GetMapping("/bsm")
    public ArrayList<String> listaBSM() {

        ArrayList<String> lista = new ArrayList<>(
                Arrays.asList("Responsabilidade Pessoal", "Persistência", "Mentalidade de Crescimento", "Orientação ao Futuro")
        );

        return lista;
    }

    @GetMapping("/objetivos")
    public ArrayList<String> listaObjetivos() {

        ArrayList<String> lista = new ArrayList<>(
                Arrays.asList("Me aperfeiçoar no Java", "Aprender testes unitários", "Me desafiar", "Desenvolver APIs úteis")
        );

        return lista;
    }

}
