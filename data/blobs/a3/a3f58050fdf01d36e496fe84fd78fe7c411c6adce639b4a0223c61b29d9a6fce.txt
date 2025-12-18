package es.ies.puerto;
/**
 * Dos equipos de héroes han recolectado botines durante una misión conjunta. 
 * Escribe un programa que combine ambos inventarios de botines en uno solo.
 * @author Shbarroso
 */
public class Ejercicio8 {
    public static void main(String[] args) {
        String[] botinEquipo1 = {"Espada mágica", "Escudo resistente"};
        String[] botinEquipo2 = {"Anillo de poder", "Armadura encantada"};

        int botinEquipo3 = botinEquipo1.length + botinEquipo2.length;
        String[] botin = new String[botinEquipo3];

        for (int i = 0; i < botinEquipo1.length; i++) {
            botin[i] = botinEquipo1[i];
        }
        for (int i = 0; i < botinEquipo2.length; i++) {
            botin[botinEquipo1.length + i] = botinEquipo2[i];
        }
        for (String botin1 : botin) {
            System.out.print(botin1 + ", ");
        }
    }
}