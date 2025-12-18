package introduction;

import java.util.Scanner;

public class Assignment3 {

	public static void main(String[] args) {

		list();
		
		System.out.println();
		
		computer();
	}
	
	public static void computer() {
		
		int row = 0, column = 0;
		double currency = 0.0, dolar = 0.0;
		boolean statusRow = false, statusCol = false;
		
		double[][] price = new double[4][6];
		
		price[0][0] = 230.21;
		price[0][1] = 400.21;
		price[0][2] = 294.2;
		price[0][3] = 693.33;
		price[0][4] = 340.44;
		price[0][5] = 691.99;
		
		price[1][0] = 529.483;
		price[1][1] = 920.483;
		price[1][2] = 676.66;
		price[1][3] = 1594.659;
		price[1][4] = 783.012;
		price[1][5] = 1591.577;
		
		price[2][0] = 552.504;
		price[2][1] = 960.504;
		price[2][2] = 706.08;
		price[2][3] = 1663.992;
		price[2][4] = 817.056;
		price[2][5] = 1660.776;

		price[3][0] = 690.63;
		price[3][1] = 1200.63;
		price[3][2] = 882.6;
		price[3][3] = 2079.99;
		price[3][4] = 1021.32;
		price[3][5] = 2075.97;
		
		String[] cpu = { "corei3", "corei5", "corei7", "corei9" };
		String[] brand = { "lenovo", "hp", "samsung", "acer", "dell", "asus" };
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Brands List : ");
		for (int j = 0; j < 6; j++) 
			System.out.print(brand[j] + "\t");
		
		System.out.println();
		
		System.out.print("Enter computer brands : ");
		String name = sc.nextLine().toLowerCase();
		
		for (int j = 0; j < 6; j++) {
			
			if (name.equals(brand[j])) {
				column = j;
				statusCol = true;
			}
		}
		
		System.out.println();
		
		if (statusCol == false) {
			
			System.out.println("Brands does not have.");
			
		}
		else {
			
			System.out.print("CPU List : ");
			for (int j = 0; j < 4; j++) 
				System.out.print(cpu[j] + "\t");
			
			System.out.println();
			
			System.out.print("Enter cpu core : ");
			String core = sc.nextLine().toLowerCase();
			
			
			
			for (int i = 0; i < 4; i++) {
				
				if (core.equals(cpu[i])) {
					row = i;
					statusRow = true;
				}
				
			}
			
			if (statusRow == false) 
				System.out.println("CPU does not have.");
			
		}
		
		System.out.println();
		
		if (statusRow == true && statusCol == true) {
			
			dolar = price[row][column];
			
			System.out.println("$" + dolar);
			
			System.out.print("Enter currency : ");
			currency = sc.nextDouble();
			
			sc.nextLine();
			
			System.out.println("Price is " + (currency * dolar)+ " MMks");
		}
			
		sc.close();
		
	}
	
	public static void list() {
		
		String[][] product = new String[5][7];
		
		product[0][0] = "Computer";
		product[0][1] = "Lenovo";
		product[0][2] = "hp   ";
		product[0][3] = "Samsung";
		product[0][4] = "Acer   ";
		product[0][5] = "Dell   ";
		product[0][6] = "Asus";
		
		product[1][0] = "Core i3";
		product[1][1] = "230.21";
		product[1][2] = "400.21";
		product[1][3] = "294.2";
		product[1][4] = "693.33";
		product[1][5] = "340.44";
		product[1][6] = "691.99";
		
		product[2][0] = "Core i4";
		product[2][1] = "529.483";
		product[2][2] = "920.483";
		product[2][3] = "676.66";
		product[2][4] = "1594.659";
		product[2][5] = "783.012";
		product[2][6] = "1591.577";
		
		product[3][0] = "Core i7";
		product[3][1] = "552.504";
		product[3][2] = "960.504";
		product[3][3] = "706.08";
		product[3][4] = "1663.992";
		product[3][5] = "817.056";
		product[3][6] = "1660.776";
		
		product[4][0] = "Core i9";
		product[4][1] = "690.63";
		product[4][2] = "1200.63";
		product[4][3] = "882.6";
		product[4][4] = "2079.99";
		product[4][5] = "1021.32";
		product[4][6] = "2075.97";
		
		System.out.println("------------------------------------------- Information List -------------------------------------------");
		
		for (var row : product) {
			
			for (var c : row)	
				System.out.print(c + "   \t");
			
			System.out.println();
			
		}
		
		System.out.println("--------------------------------------------------------------------------------------------------------");
		
	}

}