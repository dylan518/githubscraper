import java.util.Scanner;

public class Questao05 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        String str;
        char[] str_invertida;

        System.out.println("Insira uma string:");
        str= ler.nextLine();
        str_invertida=str.toCharArray();

        for (int i = str_invertida.length-1 ; i>=0 ; i--)
        {
            System.out.print(str_invertida[i]);
        }

    }
}
