package com.example.energyx.controller;

import com.example.energyx.dto.NotificacoesDTO;
import com.example.energyx.service.NotificacoesService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.stream.Collectors;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.linkTo;
import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.methodOn;

@RestController
@RequestMapping("/notificacoes")
public class NotificacoesController {
    @Autowired
    private NotificacoesService service;

    @PostMapping("/batch")
    public ResponseEntity<String> insertBatch(@RequestBody List<NotificacoesDTO> dtos) {
        service.insertBatch(dtos);
        return ResponseEntity.ok("Notificações inseridas com sucesso");
    }
}