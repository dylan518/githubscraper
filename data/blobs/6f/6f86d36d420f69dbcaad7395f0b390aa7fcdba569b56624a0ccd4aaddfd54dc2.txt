package E05;

import java.util.Scanner;

public class PrincipalT {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        System.out.println("Informe um número e mostrarei a tabuada dele: ");
        int n = sc.nextInt();

        for(int i = 1; i <= 10; i++){
            int total = n*i;
            System.out.println(n + " x " + i + " = " + total);
        }
        sc.close();
    }
}
