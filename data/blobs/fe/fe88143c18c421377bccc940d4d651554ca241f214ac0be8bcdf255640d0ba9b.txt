package com.xworkz.collectionapp;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class MoviesDTOTester {
	
	public static void main(String[] args) {
		
		MoviesDTO dto1 = new MoviesDTO("KGF", 1000, "Kannad", 100, LocalDate.of(2020, 12, 30));
		MoviesDTO dto2 = new MoviesDTO("Avatar", 2000, "English", 500, LocalDate.of(2022, 10, 17));
		MoviesDTO dto3 = new MoviesDTO("RRR", 1500, "Telagu", 300, LocalDate.of(2015, 07, 18));
		MoviesDTO dto4 = new MoviesDTO("Fana", 800, "Hindi", 80, LocalDate.of(2008, 05, 07));
		MoviesDTO dto5 = new MoviesDTO("Galipata", 1200, "Kannad", 50, LocalDate.of(2002, 11, 15));
		
		Collection<MoviesDTO> collection = Stream.of(dto1, dto2, dto3, dto4, dto5).collect(Collectors.toList());
		
		System.out.println("Sorting names in ascending order......");
		collection
		.stream()
		.sorted((a1, a2) -> a1.getName().compareTo(a2.getName()))
		.forEach(e -> System.out.println(e));
		
		System.out.println("Sorted names in descending oredr......");
		collection
		.stream()
		.sorted((a1, a2) -> a2.getName().compareTo(a1.getName()))
		.forEach(e -> System.out.println(e));
		
		System.out.println("Sorted budget in asc order.....");
		Comparator<MoviesDTO> comparator = (a1,a2) -> Double.compare(a1.getBudget(), a2.getBudget());
				collection
				.stream()
				.sorted(comparator)
				.forEach(e -> System.out.println(e));
				
		System.out.println("Sorted budget in dec order.....");
		Comparator<MoviesDTO> comparator1 = (a1, a2) -> Double.compare(a2.getBudget(), a1.getBudget());
		collection
		.stream()
		.sorted(comparator1)
		.forEach(e -> System.out.println(e));
		
		System.out.println("Sorted language in acs order");
		collection
		.stream()
		.sorted((a1, a2) -> a2.getLanguage().compareTo(a1.getLanguage()))
		.forEach(e -> System.out.println(e));
		
	}

}
