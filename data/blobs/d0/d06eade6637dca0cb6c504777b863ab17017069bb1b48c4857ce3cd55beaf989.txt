package org.design_patterns.exercices.tp_04;

import org.design_patterns.exercices.tp_04.entity.impl.Outcome;
import org.design_patterns.exercices.tp_04.entity.impl.ProgressiveTaxStrategy;
import org.design_patterns.exercices.tp_04.entity.impl.VATTaxStrategy;

import java.util.Scanner;

public class UserInterface {

    private final static Scanner sc = new Scanner(System.in);
    private static int input(int limit) {
        do {
            String input = ""+ sc.nextInt();
            if (input.matches("[0-" + limit + "]"))
                return Integer.parseInt(input);
            System.out.println("Saisie invalide");
        } while (true);
    }
    public static void mainMenu() {
        Outcome outcome = new Outcome(1500);
        int choice;
        do {
            System.out.println("""
                    ================================================
                    Simulateur de politique fiscale - Menu Principal
                    ================================================
                    
                    Choisissez une option
                    1. Sélectionnez la stratégie fiscale et lancer une simulation
                    0. Quitter""");
            if ((choice = input(1)) == 1) {
                do {
                    System.out.println("""
                            ========================================================
                               SÉLECTION DE LA STRATÉGIE FISCALE ET SIMULATION
                            ========================================================
                            
                            Choisissez une stratégie fiscale pour la simulation :
                            1. Impôt progressif sur le revenu
                            2. TVA (Taxe sur la valeur ajoutée)
                            0.Menu précédent""");
                    switch (choice = input(2)){
                        case 1 -> {
                            System.out.println("Vous avez choisi la stratégie de l'impot progressif.\nEntrez le taux de l'impot (%):");
                            outcome.useTaxStrategy(new VATTaxStrategy((double) sc.nextInt() /100));
                            System.out.println("Recettes fiscales totales de la TVA : " + outcome.getOutcomeValue() + " millions d'euros");
                        }
                        case 2 -> {
                            System.out.println("Vous avez choisi la stratégie de la TVA.\nEntrez le taux de TVA (%):");
                            outcome.useTaxStrategy(new ProgressiveTaxStrategy((double) sc.nextInt() /100));
                            System.out.println("Recettes fiscales totales de la TVA : " + outcome.getOutcomeValue() + " millions d'euros");
                        }
                    }
                } while (choice != 0);
                choice = -1;
            }
        } while (choice != 0);
    }
}
