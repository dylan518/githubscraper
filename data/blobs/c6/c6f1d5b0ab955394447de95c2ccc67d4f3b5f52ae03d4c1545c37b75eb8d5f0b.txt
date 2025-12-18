package matrizes;

public class Notas {
    public static void main(String[] args) {
        double[][] notas = {
                { 7.0, 7.5, 8.0, 7.5 },
                { 6.0, 7.5, 8.0, 8.5 },
                { 7.0, 5.5, 6.0, 7.5 }
        };

        double soma;
        for (int i = 0; i < notas.length; i++) {
            soma = 0;
            for (int j = 0; j < notas[i].length; j++) {
                soma += notas[i][j];
            }
            System.out.println("A media do aluno " + i + " é: " + soma / 4);

        }

    }
}
