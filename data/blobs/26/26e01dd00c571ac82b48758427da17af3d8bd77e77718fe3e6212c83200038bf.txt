package Opgaver.Opg2_GeneriskMetoder;

import java.util.HashSet;
import java.util.Set;

public class SetOperations {

	public static <T> Set<T> union(Set<T> s1, Set<T> s2) {
		Set<T> nySet = s1; // Opretter et nyt set og tilskriver det s1
		for (T element: s2) { // Itererer over elementerne i s2
			nySet.add(element); // Tilføjer hvert element fra s2 til nySet
		}
		return nySet; // Returnerer nySet, som er unionen af s1 og s2
	}

	public static <T> Set<T> union2(Set<T> s1, Set<T> s2) {
		Set<T> unionSet = new HashSet<>(s1); // Opretter et nyt set og tilskriver det en kopi af s1
		unionSet.addAll(s2); // Tilføjer alle elementer fra s2 til unionSet
		return unionSet; // Returnerer unionSet, som er unionen af s1 og s2
	}


	public static <T> Set<T> differens(Set<T> s1, Set<T> s2) {
		Set<T> nySet = new HashSet<>(); // Opretter et nyt set til at holde differensen af s1 og s2
		for (T element: s1) { // Itererer over elementerne i s1
			if (!s2.contains(element)) { // Hvis elementet ikke er i s2
				nySet.add(element); // Tilføjer elementet til nySet
			}
		}
		return nySet; // Returnerer nySet, som er differensen af s1 og s2
	}

	public static <T> Set<T> differens2(Set<T> s1, Set<T> s2) {
		Set<T> differensSet = new HashSet<>(s1); // Opretter et nyt set og tilskriver det en kopi af s1
		differensSet.removeAll(s2); // Fjerner alle elementer fra differensSet, som også er i s2
		return differensSet; // Returnerer differensSet, som er differensen af s1 og s2
	}


	public static <T> Set<T> intesection(Set<T> s1, Set<T> s2) {
		Set<T> nySet = new HashSet<>(); // Opretter et nyt set til at holde fællesmængden af s1 og s2
		for (T element: s1) { // Itererer over elementerne i s1
			if (s2.contains(element)) { // Hvis elementet er i s2
				nySet.add(element); // Tilføjer elementet til nySet
			}
		}
		return nySet; // Returnerer nySet, som er fællesmængden af s1 og s2
	}

}
