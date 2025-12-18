package crud;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Executora {

    public static void main(String[] args) {
        JogadoresCRUD jogCRUD = new JogadoresCRUD();
        jogCRUD.connectionDB();

        Scanner scanner = new Scanner(System.in);

        System.out.print("Escolha uma opcao: \n");
        System.out.print("Adicionar Jogador  [1] \n");
        System.out.print("Visualizar Jogador [2] \n");
        System.out.print("Atualizar Jogador  [3] \n");
        System.out.print("Deletar Jogador    [4] \n");
        int opcao = scanner.nextInt();

        switch (opcao) {
            case 1:
                System.out.print("Digite o id do Jogador: ");
                int id = scanner.nextInt();
                scanner.nextLine();
                System.out.print("Digite o nome do Jogador: ");
                String nome = scanner.nextLine();
                System.out.print("Digite o ano de treino do Jogador: ");
                int anoTreino = scanner.nextInt();
                System.out.print("Digite o salario do Jogador: ");
                float salario = scanner.nextFloat();

                if (anoTreino > 5) {
                    // veterano
                    JogadoresVeteranos jogador = new JogadoresVeteranos(id, nome, anoTreino, salario);
                    jogador.aumentarSalario();
                    jogCRUD.createJogadoresVeteranos(jogador);
                } else {
                    JogadoresTrainees jogador = new JogadoresTrainees(id, nome, anoTreino, salario);
                    jogCRUD.createJogadoresTrainees(jogador);
                }
                break;

            case 2:
                System.out.print("Visualizar Jogadores Veteranos [1] \n");
                System.out.print("Visualizar Jogadores Trainees  [2] \n");
                int opcaoVisualizar = scanner.nextInt();
                switch (opcaoVisualizar) {
                    case 1:
                        jogCRUD.readJogadoresVeteranos();
                        break;
                    case 2:
                        jogCRUD.readJogadoresTrainees();
                        break;
                    default:
                        System.out.println("Número inválido!");
                        break;
                }
                break;

            case 3:
                System.out.print("Atualizar Jogadores Veteranos [1] \n");
                System.out.print("Atualizar Jogadores Trainees  [2] \n");
                int opcaoAtualizar = scanner.nextInt();
                switch (opcaoAtualizar) {
                    case 1:
                        System.out.print("Digite qual o id do Jogador para atualizalo: ");
                        int idAtualizar = scanner.nextInt();
                        scanner.nextLine();
                        System.out.print("Digite a atualizacap do nome do Jogador: ");
                        String nomeAtualizar = scanner.nextLine();
                        System.out.print("Digite a atualizacap do ano de treino do Jogador: ");
                        int anoTreinoAtualizar = scanner.nextInt();
                        System.out.print("Digite a atualizacap do o salario do Jogador: ");
                        float salarioAtualizar = scanner.nextFloat();

                        if (anoTreinoAtualizar <= 5) {
                            jogCRUD.deleteJogadoresVeteranos(idAtualizar);
                            JogadoresTrainees jogador = new JogadoresTrainees(idAtualizar, nomeAtualizar, anoTreinoAtualizar, salarioAtualizar);
                            jogCRUD.createJogadoresTrainees(jogador);
                        } else {
                            jogCRUD.upadateJogadoresVeteranos(nomeAtualizar, anoTreinoAtualizar, salarioAtualizar, idAtualizar);
                        }
                        break;
                    case 2:
                        System.out.print("Digite qual o id do Jogador para atualizalo: ");
                        int idAtualizarTrainees = scanner.nextInt();
                        scanner.nextLine();
                        System.out.print("Digite a atualizacap do nome do Jogador: ");
                        String nomeAtualizarTrainees = scanner.nextLine();
                        System.out.print("Digite a atualizacap do ano de treino do Jogador: ");
                        int anoTreinoAtualizarTrainees = scanner.nextInt();
                        System.out.print("Digite a atualizacap do o salario do Jogador: ");
                        float salarioAtualizarTrainees = scanner.nextFloat();
                        if (anoTreinoAtualizarTrainees > 5) {
                            jogCRUD.deleteJogadoresTrainees(idAtualizarTrainees);
                            JogadoresVeteranos jogador = new JogadoresVeteranos(idAtualizarTrainees, nomeAtualizarTrainees, anoTreinoAtualizarTrainees, salarioAtualizarTrainees);
                            jogador.aumentarSalario();
                            jogCRUD.createJogadoresVeteranos(jogador);
                        } else {
                            jogCRUD.upadateJogadoresTrainees(nomeAtualizarTrainees, anoTreinoAtualizarTrainees, salarioAtualizarTrainees, idAtualizarTrainees);
                        }
                        break;
                    default:
                        System.out.println("Número inválido!");
                        break;
                }
                break;

            case 4:
                System.out.print("Deletar Jogadores Veteranos [1] \n");
                System.out.print("Deletar Jogadores Trainees  [2] \n");
                int opcaoDeletar = scanner.nextInt();
                try {
                    switch (opcaoDeletar) {
                        case 1:
                            System.out.print("Digite o id do Jogador que deseja deletar: ");
                            int idDeletar = scanner.nextInt();
                            jogCRUD.deleteJogadoresVeteranos(idDeletar);
                            break;
                        case 2:
                            System.out.print("Digite o id do Jogador que deseja deletar: ");
                            int idDeletarTrainees = scanner.nextInt();
                            jogCRUD.deleteJogadoresTrainees(idDeletarTrainees);
                            break;
                        default:
                            System.out.println("Número inválido!");
                            break;
                    }
                } catch (InputMismatchException e) {
                    System.out.println("Erro: Entrada inválida.");
                    scanner.nextLine();  // Limpar o scanner
                }
                break;

            default:
                System.out.println("Opção inválida!");
                break;
        }

        // Fechar o scanner
        scanner.close();
    }
}
