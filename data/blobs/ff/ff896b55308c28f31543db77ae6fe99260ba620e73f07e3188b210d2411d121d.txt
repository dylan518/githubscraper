package exer_2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
	public static void main(String[] args) {
		List<String> lista = new ArrayList<>();

		lista.add("tallys");
		lista.add("emanoel");
		lista.add("pedro");
		lista.add("tallys");
		lista.add("andre");
		lista.add("andre");
		lista.add("tallys");
		lista.add("tallys");
		lista.add("tallys");
		lista.add("carauta");
		
		System.out.println(countOccurrences(lista));
	}
	
	public static Map<String, Integer> countOccurrences(List<String> strings) {
		Map<String,Integer> ocorrencias = new HashMap<String, Integer>();
		
		for (int i = 0; i < strings.size(); i++) {
			if(!ocorrencias.containsKey(strings.get(i))) {
				ocorrencias.put(strings.get(i),1);
			}else {
				ocorrencias.put(strings.get(i), ocorrencias.get(strings.get(i))+1);
			}
		}
		
		return ocorrencias;
	}
}
