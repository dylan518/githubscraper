/* 3 - Uma revendedora de carros paga a seus vendedores um salário fixo por mês, mais  uma  comissão  também  fixa  para  cada  carro  vendido  e  mais  5% do  valor  das  vendas  por  ele efetuadas.
Escrever um algoritmo que leia o número de  carros por  ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor. */

import java.util.Scanner;

public class Exercicio3 {
    public static void main(String[] args) {
        // TOTAL_Salario = salario + comisao_carro + (comisao_carro + 0.05);
        Scanner entrada = new Scanner(System.in);
         double total_vendas, salario,  comissao ,total_comissao_por_carro,total_comissao_com_cinco_porcento, total_salario;

        System.out.println("Digite a quantidade de carros vendidos: ");
        int carros_vendidos = entrada.nextInt();

        System.out.println("Digite o valor total das vendas: ");
       
        total_vendas = entrada.nextDouble();

        System.out.println("Digite o salario  do colaborador: ");
        salario = entrada.nextDouble(); 

        System.out.println("Digite o valor da comissão por carro vendido: ");
        comissao = entrada.nextDouble();

        total_comissao_por_carro = comissao * carros_vendidos;
        total_comissao_com_cinco_porcento =  total_comissao_por_carro + (total_comissao_por_carro * 0.05);

        total_salario= salario + total_comissao_com_cinco_porcento; 
        System.out.println("Salario Total do colaborador: R$" + total_salario);
        
    }
}
