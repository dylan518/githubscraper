package com.maicon.trilha.EstruturaControle;

import java.util.Scanner;

public class CaixaEletronico {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double saldo = 1000.0; // Saldo inicial
        int opcao;

        do {
            // Exibe o menu de opções
            System.out.println("\n=== Caixa Eletrônico ===");
            System.out.println("1 - Consultar saldo");
            System.out.println("2 - Depositar");
            System.out.println("3 - Sacar");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = sc.nextInt();

            switch (opcao) {
                case 1:
                    // Consulta de saldo
                    System.out.printf("Saldo atual: R$ %.2f\n", saldo);
                    break;
                case 2:
                    // Depósito
                    System.out.print("Digite o valor do depósito: ");
                    double deposito = sc.nextDouble();
                    saldo += deposito;
                    System.out.printf("Depósito realizado. Novo saldo: R$ %.2f\n", saldo);
                    break;
                case 3:
                    // Saque
                    System.out.print("Digite o valor do saque: ");
                    double saque = sc.nextDouble();
                    if (saque > saldo) {
                        System.out.println("Saldo insuficiente.");
                    } else {
                        saldo -= saque;
                        System.out.printf("Saque realizado. Novo saldo: R$ %.2f\n", saldo);
                    }
                    break;
                case 0:
                    System.out.println("Encerrando o sistema...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }

        } while (opcao != 0); // Continua até o usuário digitar 0

        sc.close(); // Fecha o Scanner
    }
}
