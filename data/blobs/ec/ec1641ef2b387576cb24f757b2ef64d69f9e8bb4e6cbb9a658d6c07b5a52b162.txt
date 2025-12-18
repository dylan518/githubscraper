package Sequencial;
import java.util.Scanner;

public class circulo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double valorDoraio, area;

        System.out.print("Digite o valor do raio do circulo: ");
        valorDoraio = sc.nextDouble();


        area =Math.PI * (valorDoraio * valorDoraio);
        System.out.println("TROCO "+area);
    }
}
