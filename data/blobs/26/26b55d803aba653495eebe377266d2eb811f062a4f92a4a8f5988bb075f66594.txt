/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package bucles;

import java.util.Scanner;

/**
 *
 * @author roli1509
 */
public class ej12 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Introduce base: ");
        double base = in.nextDouble();
        System.out.println("Introduce exponenente: ");
        int expo = in.nextInt();
        double resultat = 1;

        //programa
        if (expo == 0) {
            resultat = 1;
        } else if(expo>0){
            for (int i = 0; i < expo; i++) {
                resultat *= base;
            }
        } else {
                expo=-expo;
                for (int i = 0; i < expo; i++) {
                resultat *= base;
            }
            resultat = 1 / resultat;
        }
        System.out.printf("%.2f^%d=%.2f",base,expo, resultat);

        /*
        for (int i = cont; i < b; i++) {
            a = a * a;
        }
        System.out.println(a);
         */
    }
}
