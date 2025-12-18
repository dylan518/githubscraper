package java;

import java.util.Scanner;

public class Q1117 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    double a = sc.nextDouble();
    while (a < 0 || a > 10) {
      System.out.println("nota invalida");
      a = sc.nextDouble();
    }
    double b = sc.nextDouble();
    while (b < 0 || b > 10) {
      System.out.println("nota invalida");
      b = sc.nextDouble();
    }
    System.out.printf("media = %.2f\n", (a + b) / 2);
  }

}
