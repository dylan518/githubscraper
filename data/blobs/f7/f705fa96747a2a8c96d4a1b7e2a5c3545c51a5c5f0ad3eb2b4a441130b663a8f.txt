package patterns;

import java.util.Scanner;

public class TrianglePattern3 {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int i = 1;
		int p = 1;
		while(i <= n) {
			int j = 1;
			p = i;
			while(j <= i) {
				System.out.print(p);
				j++;
				p++;
			}
			System.out.println();
			i++;
		}
		sc.close();
	}

}
