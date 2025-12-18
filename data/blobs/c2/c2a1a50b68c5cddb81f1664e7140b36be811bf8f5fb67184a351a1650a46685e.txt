package random;

import java.lang.reflect.Array;
import java.util.*;

public class randomExam01 {
	public static void main(String[] args) {

		ArrayList<Integer> arrayint = new ArrayList<>();
		HashSet<Integer> hashsetint = new HashSet<>();
		HashMap<Integer, Integer> hashmapint = new HashMap<>();

		while (true) {
			double ran = Math.random();
			int num = (int) (ran * 45) + 1;

		
			
			for (int i = 0; i<6; i++) {
				if(!arrayint.get(i).equals(num)) {
					arrayint.add(num);
				}
			}
			System.out.println(arrayint);
		}
		
	}
}