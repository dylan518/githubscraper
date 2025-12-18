import java.util.Scanner;

public class Cliente {

    String nome;
    Long cpf;
    int comprados[] = new int[1000];
    int i = 0;
    Computador comp = new Computador();
    public void calculaTotalCompra(){
        for(int j = 0; j < (i-1); j++){
            System.out.println("Voce comprou o PC da promocao " + comprados[i] );
            comp.md = comprados[i];
            comp.mostraPCConfig();
        }
    }

public static void main(String[] args) {
        int flag = 1;
        int aux;
        Cliente cl = new Cliente();
        Scanner sc = new Scanner(System.in);
        System.out.println("Bem vindo a PC mania");
        System.out.println("Qual seu nome?");
        cl.nome = sc.nextLine();
        System.out.println("Qual seu cpf?");
        cl.cpf = sc.nextLong();
        System.out.println("Gostaria de comprar um PC de nosssa promocao?");
        while(flag == 1){
            System.out.println("Qual o numero da promocao desejada?");
            aux = sc.nextInt();
            cl.comprados[(cl.i)] = aux;
            cl.calculaTotalCompra();

            System.out.println("Gostaria de sair - 0 ou ficar 1?");
            flag = sc.nextInt();
            cl.i++;
        }

        cl.calculaTotalCompra();

        }
}

