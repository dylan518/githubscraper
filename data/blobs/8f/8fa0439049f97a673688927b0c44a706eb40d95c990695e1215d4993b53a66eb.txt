package acmicpc.입출력;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem_10992 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        for (int i=1; i<=n; i++) {
            if (i == n) {
                for (int k=1; k<=2*i-1; k++) {
                    System.out.print("*");
                }
                System.out.println();
                break;
            }
            for (int j=1; j<=n-i; j++) {
                System.out.print(" ");
            }
            for (int k=1; k<=2*i-1; k++) {
                if (k == 1 || k == 2*i-1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }

            }
            System.out.println();
        }
    }
}