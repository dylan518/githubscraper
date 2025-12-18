package tp5;

public class LotissementPrivée extends Lotissement{
	
	LotissementPrivée(int capacite){
		super(capacite);
	}
	
	@Override public boolean ajouter(Propriete p) {
		if(p instanceof PropriétéPrivée ) {
			if(nombre<tabProp.length) {
				tabProp[nombre]=p;
				nombre++;
			}
		return true;
		}
		else {
			return false;
		}
	}
	
	

	@Override public PropriétéPrivée getpropriétéByIndice (int k) {
		if (k >= 0 && k < tabProp.length && tabProp[k] instanceof PropriétéPrivée) {
	        return ((PropriétéPrivée)tabProp[k]);
	    } else {
	        return null;
	    }
	}
		
	
	@Override  int getnbPièces() {
		int nbr=0 ;
		for(int i =0;i<tabProp.length;i++) {
			if(tabProp[i] instanceof PropriétéPrivée) {
				nbr+=((PropriétéPrivée)tabProp[i]).nbPieces;
			}
		}
		return nbr;
		
	}
}
