/*Faça um Programa que peça os 3 lados de um triângulo. O programa
        deverá informar se os valores podem ser um triângulo. Indique, caso
        os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou
        escaleno.
        o Dicas:
        o Três lados formam um triângulo quando a soma de quaisquer
        dois lados for maior que o terceiro;
        o Triângulo Equilátero: três lados iguais;
        o Triângulo Isósceles: quaisquer dois lados iguais;
        o Triângulo Escaleno: três lados diferentes;*/
package exercicio02;

import java.util.Scanner;

public class Exercicio15 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("INFORME 3 MEDIDAS, PARA EU CALCULAR SE É UM TRIANGULO OU NÃO, E O SEU TIPO.");
        System.out.print("MEDIDA 1: ");
        double lado1 = input.nextDouble();
        System.out.print("MEDIDA 2: ");
        double lado2 = input.nextDouble();
        System.out.print("MEDIDA 3: ");
        double lado3 = input.nextDouble();

        if (lado1 + lado2 > lado3 && lado2 + lado3 > lado1 && lado1 + lado3 > lado2){
            System.out.println("É um TRIANGULO!");
            if (lado1 == lado2 && lado2 == lado3) {
                System.out.println("É um TRIANGULO EQUILÁTERO!");
            } else if (lado1 == lado2 || lado2 == lado3 || lado1 == lado3) {
                System.out.println("É um TRIANGULO ISÓSCELES!");
            } else {
                System.out.println("É um TRIANGULO ESCALENO!");
            }
        }else {
            System.out.println("Não é um TRIANGULO!");
        }

    }
}
