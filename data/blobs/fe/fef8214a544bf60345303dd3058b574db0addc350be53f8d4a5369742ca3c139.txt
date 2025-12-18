import java.util.Scanner;

public class Leitura {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);

        System.out.println("Digite seu filme favorito: ");
        String filme = leitura.nextLine();

        System.out.println("Fale a Sinopse do filme : ");
        String sinopse = leitura.nextLine();

        System.out.println("Digite um ano de Lançamento : ");
        int anoDeLancamento = leitura.nextInt();

        System.out.println("Digite a avaliação do fime : ");
        double avaliacao = leitura.nextDouble();

        System.out.println("Seu Filme Favorito é " + filme + " e o ano de laçamento foi  " + anoDeLancamento + " E sua avaliação foi de " + avaliacao + " Sinopse: " + sinopse);

    }
}
