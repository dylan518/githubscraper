package aula_19.exercicios;

import java.util.Scanner;

/**
 * Exercicio_33
 * 
 * Criar um vetor A com 10 elementos inteiros. Escreva um programa que imprima
 * cada elemento do vetor A e uma mensagem indicando se o respectivo elemento é
 * um número primo ou não.
 * 
 * @author Germano-Silva
 *
 */
public class Exercicio_33 {

	public static void main(String[] args) {
		try (Scanner scan = new Scanner(System.in)) {
			int[] a = new int[5];
			boolean primo = true;
			String msg = "";
			
			for (int i = 0; i < a.length; i++) {
				System.out.println("Entre com um número para a posição A = " + i);
				a[i] = scan.nextInt();
			}
			
			
			for (int i = 0; i < a.length; i++) {
				for (int j = 2; j < a[i]; j++) {
					if(a[i]%j==0) {
						primo = false;
						break;
					}
				}
				
				if (primo) {
					msg = "Primo";
				} else {
					msg = "Não é primo";
				}
				
				System.out.println(a[i] +" "+ msg);
			}
		}
	}
}
