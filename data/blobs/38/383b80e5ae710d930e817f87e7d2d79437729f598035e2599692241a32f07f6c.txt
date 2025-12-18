package com.example.rpg_v2;//Programme de Baptiste Reynaud

//Les fonctions qu'il manque : l'ennemi nous attaque, combat contre le boss à la fin une fois que tous les autres ennemies sont morts, le hunter a un nombre de flèches limité, partie combat de l'interface


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Voulez-vous jouer dans la console ou dans l'interface ?" + "\n" + "Taper 1 pour la console et 2 pour l'interface : ");

        int choice = sc.nextInt();
        if (choice == 1){
            Game.Play();
        }else{
            HelloApplication.main();

        }
    }
}