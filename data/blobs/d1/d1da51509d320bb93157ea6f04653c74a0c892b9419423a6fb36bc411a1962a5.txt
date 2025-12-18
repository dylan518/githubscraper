package com.mycompany.caixaeletronica;

import javax.swing.JOptionPane;

public class CaixaEletronica {

    public static void main(String[] args) {
        Conta conta = new Conta();
        boolean b = true;
        int opcao = 0;
        double saque;
        double deposito;

        do {
            opcao = Integer.parseInt(JOptionPane.showInputDialog(null, "escolha uma opcao: \n1. Saque\n2. Depósito\n3. Extrato\n4. Criar conta"));

            switch (opcao) {
                case 1:
                    saque = Double.parseDouble(JOptionPane.showInputDialog("Digite um valor para sacar "));
                    conta.sacar(saque);
                    break;
                case 2:
                    deposito = Double.parseDouble(JOptionPane.showInputDialog("Digite um valor para deposito "));
                    conta.deposito(deposito);
                    break;
                case 3:
                    conta.extrato();
                    break;
                case 4:
                    conta.criarConta();
                    break;
                default:
            }

        } while (b == true);
    }
}
