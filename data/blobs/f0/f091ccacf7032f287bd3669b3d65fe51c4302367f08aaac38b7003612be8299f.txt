/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.ProyectoF1.proyectof1.model;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.util.List;
import java.util.Set;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.OneToMany;
import javax.persistence.Table;

/**
 *
 * @author Gregsoft
 */
@Entity
@Table(name="Tbl_circuito")
public class Circuito {
     
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "circuitoId", nullable = false)
    private Integer id;
    
     @Column(name = "nombre", nullable = false, length = 150)
    private String nombre; 
     @Column(name = "ciudad", nullable = false, length = 150)
    private String ciudad;
     @Column(name = "pais", nullable = false, length = 150)
    private String pais;
     @Column(name = "trazado", nullable = false, length = 150, columnDefinition = "LONGTEXT")
    private String trazado;
     @Column(name = "numeroVueltas", nullable = false)
    private int numeroVueltas;
     @Column(name = "longitud", nullable = false)
    private double longitud;
     @Column(name = "curvasLentas", nullable = false)
    private int curvasLentas;
     @Column(name = "curvasMedia", nullable = false)
    private int curvasMedia;
     @Column(name = "curvasRapidas", nullable = false)
    private int curvasRapidas;
        @Column(name = "foto", nullable =true, columnDefinition = "LONGTEXT")
    private String foto;
    @OneToMany(mappedBy = "circuito", fetch = FetchType.EAGER)
    @JsonIgnoreProperties(value = {"Tbl_circuito"})
    private List<Carrera> carrera;
    
    public Circuito() {
    }

    public Circuito(String nombre, String ciudad, String pais, String trazado, int numeroVueltas, double longitud, int curvasLentas, int curvasMedia, int curvasRapidas, String foto) {
        this.nombre = nombre;
        this.ciudad = ciudad;
        this.pais = pais;
        this.trazado = trazado;
        this.numeroVueltas = numeroVueltas;
        this.longitud = longitud;
        this.curvasLentas = curvasLentas;
        this.curvasMedia = curvasMedia;
        this.curvasRapidas = curvasRapidas;
        this.foto = foto;
    }

    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }



    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    public String getTrazado() {
        return trazado;
    }

    public void setTrazado(String trazado) {
        this.trazado = trazado;
    }

    public int getNumeroVueltas() {
        return numeroVueltas;
    }

    public void setNumeroVueltas(int numeroVueltas) {
        this.numeroVueltas = numeroVueltas;
    }

    public double getLongitud() {
        return longitud;
    }

    public void setLongitud(double longitud) {
        this.longitud = longitud;
    }

    public int getCurvasLentas() {
        return curvasLentas;
    }

    public void setCurvasLentas(int curvasLentas) {
        this.curvasLentas = curvasLentas;
    }

    public int getCurvasMedia() {
        return curvasMedia;
    }

    public void setCurvasMedia(int curvasMedia) {
        this.curvasMedia = curvasMedia;
    }

    public int getCurvasRapidas() {
        return curvasRapidas;
    }

    public void setCurvasRapidas(int curvasRapidas) {
        this.curvasRapidas = curvasRapidas;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
    
    
}
