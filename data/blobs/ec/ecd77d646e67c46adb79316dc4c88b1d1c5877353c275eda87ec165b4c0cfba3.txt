import java.util.Random;

//11.Criar um vetor A com 10 elementos inteiros. Implementar um programa que //defina e escreva a quantidade de elementos armazenados neste vetor que são //pares.

import java.util.Random;

public class Exercicio11 {
	public static void main(String[] args) {

		int[] vetorA = new int[10];
		int quantidadeDePares = 0;
		Random random = new Random();

//Este for está armazenando um valor aleatório de 0 a 99 dentro das posições do vetor A.

		for (int i = 0; i < vetorA.length; i++) {
			vetorA[i] = random.nextInt(100);

			if (vetorA[i] % 2 == 0) {
				quantidadeDePares++;
			}

		}
		System.out.println("A quantidade de pares do vetor é: " + quantidadeDePares);
	}

}

		
	


