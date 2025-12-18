package pl.edu.pw.mini.po.grzybobranie;

import java.util.Random;

public class MuchomorKolczastoglowy extends Muchomor{

	Random random = new Random();
	
	public MuchomorKolczastoglowy() {
		this.twardosc = Twardosc.values()[random.nextInt(3)];
		this.masaOwocnika = random.nextDouble(25) + 25;
	}	

	@Override
	public void wypiszMuchomora() {
		super.wypiszMuchomora();
		System.out.println("nazwa: muchomor kolczastoglowy");
		 
	}
	
	@Override
	public String toString() {
		return super.toString() + "/nnazwa: muchomor kolczastoglowy";
	}
}
