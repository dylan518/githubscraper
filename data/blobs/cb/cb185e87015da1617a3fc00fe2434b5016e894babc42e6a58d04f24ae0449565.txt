package co.edu.poli.usertaller1.persistence.entity;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import jakarta.persistence.*;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import lombok.Getter;
import lombok.Setter;

import java.util.List;
import java.util.Objects;

@Getter
@Setter
@Entity
@Table(name = "filas")
public class Fila {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id_fila")
    private Integer idFila;


    /*@OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "id_tarea")
    private Tarea tarea;*/

    @JsonManagedReference
    @OneToOne(mappedBy = "fila",fetch = FetchType.EAGER, cascade = CascadeType.ALL)
    private Tarea tarea;

    @Column(name = "duracion")
    @Min(value = 1, message = "La duración debe ser mayor o igual a 1")
    @Max(value = 60, message = "La duración debe ser menor o igual a 60")
    private Integer duracion;

    @JsonBackReference
    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_usuario")
    private Usuario usuario;




    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Fila fila = (Fila) o;
        return Objects.equals(idFila, fila.idFila);
    }

    @Override
    public int hashCode() {
        return Objects.hash(idFila);
    }

}
