package br.com.edusync.Spring.Models;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity ( name = "tb_veterinario")
public class Veterinario {


    private String nome;
    @Id
    private Integer CRN;
    @ManyToOne
    @JoinColumn
    private Clinica clinica;
}
