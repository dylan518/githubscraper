import java.util.Scanner;

public class Constantes {

    static final Integer IDADE_MINIMA_PARA_TIRAR_CARTEIRA = 18;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //final Integer idadeMinimaParaTirarCarteira = 18; // o "final" é usado para fazer uma variavel se manter constante

        System.out.print("Idade: ");
        Integer idade = scanner.nextInt();

        Boolean podeTiraCarteira = idade >= IDADE_MINIMA_PARA_TIRAR_CARTEIRA;

        if (podeTiraCarteira) {
            System.out.println("Sim! Ele pode tirar a carteira");
        } else {
            System.out.println("Não! Ele não pode tirar a carteira");
        }
        scanner.close();
    }
}
