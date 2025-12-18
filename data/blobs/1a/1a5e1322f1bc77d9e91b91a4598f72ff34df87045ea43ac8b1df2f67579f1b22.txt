package com.geriatria.app.persistence.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalTime;
import java.util.List;

@Entity
@Table(name = "paciente")
@Getter
@Setter
@NoArgsConstructor
public class PacienteEntity {
    @Id
    @Column(name="id_paciente")
    private String idPaciente;

    @Column(name = "nombre", length = 55)
    private String nombre;

    @Column
    private Integer edad;

    @OneToMany(mappedBy = "paciente",fetch = FetchType.LAZY)
    private List<PacienteActividadEntity> actividadespaciente;

    /*
    @OneToMany(mappedBy = "paciente",fetch = FetchType.LAZY)
    private List<RegistroEntity> registros;*/



}
