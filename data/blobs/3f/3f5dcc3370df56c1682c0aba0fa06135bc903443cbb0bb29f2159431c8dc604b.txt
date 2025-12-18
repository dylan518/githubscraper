package com.facens.ac2b.model.entity;


import jakarta.persistence.*;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Curso {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "idcurso")
    private Long idCurso;

    private String name;

    private String description;

    private float workLoad;

    private String objectives;

    private String ementa;

    @OneToMany(mappedBy = "curso")
    List<Agenda> agendList;

    @ManyToMany
    @JoinTable(name = "professor_curso",
            joinColumns = @JoinColumn(name = "professorid"),
            inverseJoinColumns = @JoinColumn(name = "cursoid"))
    List<Professor> professorList;
}
