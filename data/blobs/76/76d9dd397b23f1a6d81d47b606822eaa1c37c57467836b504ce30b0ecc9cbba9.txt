package application;

import java.util.Locale;
import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		
			Locale.setDefault(Locale.US);
			Scanner sc = new Scanner(System.in);
			
			int n;
			System.out.println("Quantas pessoas serao digitadas? ");
			n = sc.nextInt();
			
			double[] vetorAltura = new double[n];
			char[] vetorGenero = new char[n];
			
			for (int i = 0; i < vetorGenero.length; i++) {
				System.out.print("Altura da " + (i+1) + "a pessoa: ");
				vetorAltura[i] = sc.nextDouble();
				System.out.print("Genero da " + (i+1) + "a pessoa: ");
				vetorGenero[i] = sc.next().charAt(0);
			}
			
			double maior_altura = vetorAltura[0];
			double menor_altura = vetorAltura[0];
			int total_mulheres = 0;
			double altura_mulheres = 0.0;
			
			for (int i = 0; i < vetorAltura.length; i++) {
				if (vetorAltura[i] > maior_altura) {
					maior_altura = vetorAltura[i];
				} 
				
				if (vetorAltura[i] < menor_altura) {
					menor_altura = vetorAltura[i];
				}
				
				if (vetorGenero[i] == 'F') {
					altura_mulheres += vetorAltura[i];
					total_mulheres++;
				}
			}
			
			System.out.printf("Menor altura = %.2f%n", menor_altura);
			System.out.printf("Maior altura = %.2f%n", maior_altura);
			System.out.printf("Media das alturas das mulheres = %.2f%n", (altura_mulheres/total_mulheres));
			System.out.println("Numero de homens = " + (vetorGenero.length - total_mulheres));
			
			sc.close();
	}

}
