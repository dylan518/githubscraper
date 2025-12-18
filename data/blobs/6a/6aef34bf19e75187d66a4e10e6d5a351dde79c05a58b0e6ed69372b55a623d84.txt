package lesson006;

public class Question49 {

	public static void main(String[] args) {
		// tek sayıları farklı bir arrayin içine atalım
		int[][] matris = { { 56, 23, 678, 231, 5, 3 }, { 234, 21, 78, 26, 6, 4 }, { 654, 33, 32, 67, 2, 5 },
				{ 189, 35, 56, 89, 8, 6 }, { 189, 35, 56, 89, 8, 6 }, { 189, 33, 59, 89, 1, 7 }, };
		
		//6x6 bir matris var burada... toplam 36 sayı var.
		// daha dinamik olsun,
		// matris.length * matris[0]*.length lik bir matris oluşturalm:
		

		int index = 0;
		int[] tekSayilar = new int[matris.length * matris[0].length];
		// int[] tekSayilar2 = new int[30];
		// int[] tekSayilar2 = {23 _ _ _ _ _ _ _ _ _ _ _ _ _ __ _ _ }
		for (int i = 0; i < matris.length; i++) {
			for (int j = 0; j < matris[i].length; j++) {
				if (matris[i][j] % 2 != 0) {// tek mi kontrol et 
					tekSayilar[index++] = matris[i][j]; // yaz kaç sayı varsa o kadarlık tekSayilar dizisine
					// ilk bulduğunu yaz.
				}
			}

		}
		
		for (int j = 0; j < matris.length * matris[0].length; j++) { // bu toplam kaçlık oluşturduysa diziyi hepsini yazar.
		
			System.out.print(tekSayilar[j] + " ");
			
		}

		System.out.println();
		
		for (int j = 0; j < index ; j++) {
			System.out.print(tekSayilar[j] + " ");
			
		}
	}

}
