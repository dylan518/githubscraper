
package com.test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

import org.omg.CosNaming.IstringHelper;

public class DecreasingOrder {

	public static void main(String[] args) {

		int n=4561103;//output=6543
        ArrayList<Integer> al=new ArrayList<Integer>();
		while(n!=0)
		{
			int d=n%10;
			al.add(d);
			n=n/10;
		}
		Collections.sort(al);
		int max=0;
		for(int i=al.size()-1 ; i>=0;i--)
		{
			max=max*10+al.get(i);
		}
		System.out.println(max);
		
//		String s=""+n;
//		char [] ch=s.toCharArray();
//		Arrays.sort(ch);
//		int max=Integer.parseInt(new StringBuilder(new String(ch)).reverse().toString());
//		System.out.println(max);
	}

}
