import java.util.Scanner;

public class Aufgabe3 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.print("Zahl: ");
		int n = s.nextInt();
		s.close();
		int ergebnis = quersumme(n);
		System.out.println("Quersumme: " + ergebnis);
	}

	public static int quersumme(int n) {
		int quersumme = 0;
		while (n != 0) {
			quersumme = quersumme + (n % 10);
			n = n / 10;
		}
		return (quersumme);
	}
}
