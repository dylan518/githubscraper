package com.ashvinimadamproblems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ConvertArrayToarrayList {
	
	public static void main(String[] args) {
		
		String s[]= {"Surat", "Mumbai", "Pune" };
		
		
		List<String> list =new ArrayList<String>( Arrays.asList(s));
		
		
		
		System.out.println(list);
		
		list.add("Amravati");
		list.add("Daryaour");
		
		System.out.println(list);
		
		
		
		
		
	


}}