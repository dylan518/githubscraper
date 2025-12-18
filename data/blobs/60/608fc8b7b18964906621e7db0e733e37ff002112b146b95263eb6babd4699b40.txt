package barbeariaCorteNinja;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main extends JFrame {

    public Main() {
        // Configurações básicas da janela
        setTitle("Barbearia Corte Ninja");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Layout da janela
        setLayout(new GridLayout(5, 1));

        // Botões
        JButton btnInstalar = new JButton("Instalar (Criar Arquivo)");
        JButton btnExcluirCadastro = new JButton("Excluir Cadastro");
        JButton btnRealizarVenda = new JButton("Realizar Venda");
        JButton btnVerCadastro = new JButton("Ver Cadastro de Cliente");
        JButton btnCadastrarCliente = new JButton("Cadastrar Cliente");

        // Adicionando botões à janela
        add(btnInstalar);
        add(btnExcluirCadastro);
        add(btnRealizarVenda);
        add(btnVerCadastro);
        add(btnCadastrarCliente);

        // Ações dos botões
        btnInstalar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                CriarArquivo.criar();
            }
        });

        btnExcluirCadastro.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nomeExcluir = JOptionPane.showInputDialog("Digite o nome do cliente que deseja excluir:");
                if (nomeExcluir != null && !nomeExcluir.isEmpty()) {
                    if (Eliminar.excluirCliente(nomeExcluir)) {
                        JOptionPane.showMessageDialog(null, "Cliente " + nomeExcluir + " excluído com sucesso.");
                    } else {
                        JOptionPane.showMessageDialog(null, "Cliente " + nomeExcluir + " não encontrado.");
                    }
                }
            }
        });

        btnRealizarVenda.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nomeCliente = JOptionPane.showInputDialog("Digite o nome do cliente:");
                String opcaoServico = JOptionPane.showInputDialog("Escolha o serviço (corte/barba/combo):");

                if (nomeCliente != null && !nomeCliente.isEmpty() && opcaoServico != null && !opcaoServico.isEmpty()) {
                    Vender.realizarVenda(nomeCliente, opcaoServico);
                }
            }
        });

        btnVerCadastro.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nomeCliente = JOptionPane.showInputDialog("Digite o nome do cliente que deseja ver:");
                if (nomeCliente != null && !nomeCliente.isEmpty()) {
                    LerArquivo.verCadastroCliente(nomeCliente);
                }
            }
        });

        btnCadastrarCliente.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nomeCliente = JOptionPane.showInputDialog("Digite o nome e sobrenome do cliente:");
                String emailCliente = JOptionPane.showInputDialog("Digite o email do cliente:");
                String numeroCliente = JOptionPane.showInputDialog("Digite o número do cliente:");

                if (nomeCliente != null && !nomeCliente.isEmpty() && 
                    emailCliente != null && !emailCliente.isEmpty() && 
                    numeroCliente != null && !numeroCliente.isEmpty()) {
                    
                    if (LerArquivo.isNomeCadastrado(nomeCliente)) {
                        JOptionPane.showMessageDialog(null, "Nome já cadastrado no sistema.");
                    } else {
                        Gravar.setTexto(nomeCliente);
                        Gravar.main(null);

                        Gravar.setTexto(emailCliente);
                        Gravar.main(null);

                        Gravar.setTexto(numeroCliente);
                        Gravar.main(null);

                        JOptionPane.showMessageDialog(null, "Cliente cadastrado com sucesso.");
                    }
                }
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Main().setVisible(true);
            }
        });
    }
}
