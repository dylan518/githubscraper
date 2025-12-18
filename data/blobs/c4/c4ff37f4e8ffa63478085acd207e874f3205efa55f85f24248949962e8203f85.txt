/*
    Ler N valores interios (N <= 100) até que seja digitado o valor zero
 */

import java.util.Arrays;
import java.util.Scanner;

public class Exercicio02
{
    public static void main(String[] args)
    {
        Scanner entrada = new Scanner(System.in);
        int aux, qtd = 0;

        int [] A = new int[100];
        for (int i = 0; i < A.length; i++)
        {
            System.out.printf("Digite o %d° elemento ou zero para encerrar: ", i+1);
            aux = entrada.nextInt();
            if(aux != 0)
            {
                A[i] = aux;
                qtd++;
            }
            else break;
        }

        int cont = qtd - 1;
        for (int i = 0; i < qtd/2; i++, cont--)
        {
            aux = A[i];
            A[i] = A[cont];
            A[cont] = aux;
        }
        
        System.out.print("Vetor: [");
        for (int i = 0; i < qtd; i++)
        {
            System.out.printf("%d, ", A[i]);
        }
        System.out.print("]");
    }
}
