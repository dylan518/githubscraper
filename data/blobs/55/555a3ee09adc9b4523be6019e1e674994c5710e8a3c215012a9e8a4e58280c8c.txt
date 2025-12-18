
public class Note {

	private static final int Note_Maximum=20;
	private double valeur ;
	private boolean estAbsent;
	
	public Note(double valeur, boolean estAbsent) {
		super();
		if (valeur>=0 && valeur<=Note_Maximum) {
		this.valeur = valeur;
		this.estAbsent = estAbsent;
	}
	
	}
	
	public Note() {
		this.valeur=0;
		this.estAbsent=true;
}
	public Note(double valeur) {
		if (valeur>=0 && valeur<=Note_Maximum) {
			this.valeur = valeur;
			this.estAbsent=false;
	}
}

	public double getValeur() {
		return valeur;
	}

	public void setValeur(double valeur) {
		this.valeur = valeur;
	}

	public boolean isEstAbsent() {
		return estAbsent;
	}

	public void setEstAbsent(boolean estAbsent) {
		this.estAbsent = estAbsent;
	}

	public static Note moyennesNotes(Note []notes) {
		double sum=0;
		int count=0;
		boolean estAbsent=false;
		for(Note note:notes) {
			if(note==null) {
				estAbsent=true;
			}else {
				sum+=note.getValeur();
				count++;
		   }
		}
		if(estAbsent) {
			return null;
		}else {
			Note moy=new Note(sum/count);
			return moy;
		}
	}
	
	
	@Override
	public String toString() {
		
		if(estAbsent) {
			return "ABS";
		}else {
			return valeur +"/20";
		}
	}
	
	
	
}
