package com.digitalhouse.junit.vivo;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PersonaTest {

    @Test
    void mostrarNombreCompleto(){
        Persona eliana = new Persona("Eliana","Valderrama","mail@mail.com",36);
        String respuestaEsperada = "Nombre completo: Valderrama, Eliana";
        String respuestaObtenida = eliana.mostrarNombre();
        Assertions.assertEquals(respuestaEsperada,respuestaObtenida);

    }

    @Test
    void calcularMayorEdad(){
        Persona eliana = new Persona("Eliana","Valderrama","mail@mail.com",36);
        Assertions.assertTrue(eliana.calcularEdad());
    }

}