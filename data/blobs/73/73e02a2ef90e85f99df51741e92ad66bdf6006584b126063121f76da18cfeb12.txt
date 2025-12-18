package org.iesvdm.pruebaud3.dao;

import lombok.extern.slf4j.Slf4j;
import org.iesvdm.pruebaud3.modelo.Pelicula;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;

//Anotación lombok para logging (traza) de la aplicación
@Slf4j
//Un Repository es un componente y a su vez un estereotipo de Spring para el CRUD
//que forma parte de la ‘capa de persistencia con  Acceso a BBDD’.
@Repository
public class PeliculaDAOImpl implements PeliculaDAO{

    //Plantilla jdbc inyectada automáticamente por el framework Spring, gracias a la anotación @Autowired.
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Override
    public List<Pelicula> getAll() {

        List<Pelicula> listPeli = jdbcTemplate.query(
                "SELECT * FROM pelicula",
                (rs, rowNum) -> new Pelicula(
                        rs.getInt("id_pelicula"),
                        rs.getString("titulo"),
                        rs.getString("descripcion"),
                        rs.getDate("fecha_lanzamiento"),
                        rs.getInt("id_idioma"),
                        rs.getInt("duracion_alquiler"),
                        rs.getDouble("rental_rate"),
                        rs.getInt("duracion"),
                        rs.getDouble("replacement_cost"),
                        rs.getDate("ultima_actualizacion")
                )
        );

        log.info("Devueltos {} registros.", listPeli.size());

        return listPeli;

    }






}
