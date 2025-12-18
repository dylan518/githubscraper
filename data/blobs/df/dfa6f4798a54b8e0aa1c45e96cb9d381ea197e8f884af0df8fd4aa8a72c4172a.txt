package desafio_4;

import java.util.Scanner;

public class Main {

public static void main(String[] args) {

	Scanner sc = new Scanner(System.in);

	int n = sc.nextInt();
	sc.nextLine();

  for (int i = 0; i < n; i++) {
	String line = sc.nextLine();
	int len = line.length();
	StringBuilder linhaDecifrada = new StringBuilder();

  for (int j = len / 2 - 1; j >= 0; j--) {
    linhaDecifrada.append(line.charAt(j));
  }

  for (int j = len - 1; j >= len / 2; j--) {
    linhaDecifrada.append(line.charAt(j));
  }

  System.out.println(linhaDecifrada.toString());
	}

	sc.close();

	}
}
