package lacosCondicionais;

import java.util.Scanner;

public class exercicio7 {

	public static void main(String[] args) {

		Scanner leia = new Scanner(System.in);
		
		String dados, n1, n2;
		float num1, num2, soma, subtracao, multiplicacao, divisao;
		int cod;
		
		System.out.println("Defina dois números (A-B).");
		dados = leia.next();
		System.out.println("\nEscolha uma operação:\n1 - Soma;\n2 - Subtração;\n3 - Multiplicação;\n4 - Divisão.");
		cod = leia.nextInt();
		
		if (cod < 1 || cod > 4){
			System.out.println("\nOPÇÃO INVÁLIDA!\nEscolha uma operação:\n1 - Soma;\n2 - Subtração;\n3 - Multiplicação;\n4 - Divisão.");
			cod = leia.nextInt();
		}
		
		String[] dados1 = dados.split("-");
		n1 = dados1[0]; n2 = dados1[1];
		num1 = Float.parseFloat(n1); num2 = Float.parseFloat(n2);
		
		switch (cod) {
		case 1:
			soma = num1 + num2;
			System.out.println(num1 + " + " + num2 + " = " + soma);
		break;
		case 2:
			subtracao = num1 - num2;
			System.out.println(num1 + " - " + num2 + " = " + subtracao);
		break;
		case 3:
			multiplicacao = num1 * num2;
			System.out.println(num1 + " * " + num2 + " = " + multiplicacao);
		break;
		case 4:
			divisao = num1 / num2;
			System.out.println(num1 + " / " + num2 + " = " + divisao);
		break;
		
		}
		
	}

}
