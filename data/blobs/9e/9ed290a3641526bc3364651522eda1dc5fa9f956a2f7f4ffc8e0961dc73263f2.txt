package com.mkpits.collection;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class IntegerArrayListClass {

	public static void main(String[] args)  {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter num how many element you want to add :");

		try {
			int range=Integer.parseInt(br.readLine());
			Integer []intArr = new Integer[range];
			for (int i = 0; i < range; i++) {
				System.out.println("Enter number :");
				intArr[i]=Integer.parseInt(br.readLine());
			}
			PrintSum<Integer> printIntArr=new PrintSum<>();
			printIntArr.print(intArr);
			
				
			}catch(IOException obj){
				obj.printStackTrace();
			}
		
//		for (Integer integer : intArr) {
//			System.out.println(integer);
//		}
		
		
		
	}
	}
	


