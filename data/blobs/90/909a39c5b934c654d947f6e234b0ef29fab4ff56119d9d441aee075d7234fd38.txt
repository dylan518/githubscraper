package com.softtek.modelo;

import java.util.function.Function;

public class ProbarFunctionValidacion {

    private void validarContrasena() {
        String contrasenia = "Contrasenia123!";

        Function<String, Boolean> ochoCaracteres = str -> str.length() >= 8;
        Function<String, Boolean> mayuscula = str -> str.matches(".*[A-Z].*");
        Function<String, Boolean> minuscula = str -> str.matches(".*[a-z].*");
        Function<String, Boolean> numero = str -> str.matches(".*\\d.*");
        Function<String, Boolean> caracterEspecial = str -> str.matches(".*[!@#$%^&*()].*");

        boolean esValida = ochoCaracteres.apply(contrasenia) &&
                mayuscula.apply(contrasenia) &&
                minuscula.apply(contrasenia) &&
                numero.apply(contrasenia) &&
                caracterEspecial.apply(contrasenia);

        System.out.println("contraseña :" + (esValida ? "válida" : "inválida"));
    }

    public static void main(String[] args) {
        ProbarFunctionValidacion app = new ProbarFunctionValidacion();
        app.validarContrasena();
    }
}

