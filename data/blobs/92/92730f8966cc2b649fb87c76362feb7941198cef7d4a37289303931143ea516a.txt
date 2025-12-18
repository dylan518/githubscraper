package helloword;

public class Recap1 {
	public static void main(String[] args) {
		// Tipuri de date primitive

		int numarintreg = 50; // am Declarar si Initializat o variabila
		short numarmaimic = -32456; // short se refera la un numar mai mic pt pc.
		long numarmare = 922337202; // long se refera la un numar mai mare decat short si int

		double numarfractionar = 7.432; // double se refera la numere fractionare/zecimale
		float numarfractionar2 = 322.4f; // diferenta dintre double si float este ca float este pe 32 de bit si double
											// 64.(double poate reprezenta un numar mai mare x2 fata de float.)

		char carcater = 'a'; // acesta comanda poate reprezenta un singur caracter (!trebuie sa fie
								// inconjurat de ''!)
		boolean adevaratsaufals = true; // aceasta comanda poate stoca valori reale sau false.

		byte bytemaxmin = 127; // poate avea o valoare maxima de 127 si una minima de -128.

		// Strings (nu este un tip de data !doar la java!) - string este o clasa

		String text = "acesta este un string";

		String spatiuliber = " ";

		String nume = "costica";

		String propozitie = text + spatiuliber + nume; // concatenare am concatenat aceste variabile de tip text.

		System.out.println("urmeaza o propozitie:" + "\n\t" + propozitie); // poti face inauntrul lui \n(new line) si
																			// \t(tab)

		int value = 0;

		while (value < 10) {
			System.out.println("hello" + value);
			// if u run this you get an infinite loop!

			//value = value + 1; // la fel
			value++;

			// for loops


		}
		
		for (int i = 0; i < 5; i++) {
            
			System.out.printf("the value of i is: %d\n", i);
		}
		
		
	}

}
