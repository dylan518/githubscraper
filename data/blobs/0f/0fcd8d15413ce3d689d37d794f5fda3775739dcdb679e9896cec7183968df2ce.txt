/*Escreva um programa que receba um ano e determine se é bissexto ou não. Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.*/
package PALista1;
import java.util.Scanner;

public class Exercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int ano = 0;

        do {
            System.out.println("Digite um ano qualquer ou '0' para sair:");
            ano = scanner.nextInt();

            if (ano != 0) {
                if (ano % 4 == 0) {
                    System.out.println("O ano " + ano + " é bissexto!");
                } else if (ano % 100 != 0){
                    System.out.println("O ano " + ano + " não é bissexto!");
                } else if (ano % 400 == 0){
                    System.out.println("O ano " + ano + " é bissexto!");    
                }
            }
        } while (ano != 0);
        scanner.close();
    }
}
