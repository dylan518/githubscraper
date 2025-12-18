package fr.diginamic.banque.entites;

import fr.diginamic.banque.entites.Compte;

public class CompteTaux extends Compte {
	
	
	private double tauxRemuneration;
	
	public CompteTaux (String numero, double solde, double tauxRemuneration ) {
		
		super(numero,solde);
		this.tauxRemuneration=tauxRemuneration;
		
		
	}
	@Override
	public String toString() {
		String chaine = super.toString();
		return  chaine + ", tauxRemuneration=" + tauxRemuneration + "]";
		
	}
	public double getTauxRemuneration() {
		return tauxRemuneration;
	}
	public void setTauxRemuneration(double tauxRemuneration) {
		this.tauxRemuneration = tauxRemuneration;
	}

	
	

}
