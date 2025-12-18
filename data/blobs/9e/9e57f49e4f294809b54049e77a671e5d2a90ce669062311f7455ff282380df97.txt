public class Entraineur extends Personne{
    private int numeroDelicence;
    Entraineur(String nom, String prenom, String adresse, int numeroDelicence){
        super(nom, prenom, adresse);
        this.numeroDelicence=numeroDelicence;
    }
    public String toString() {
        return super.toString() +"\nNumero de licence: "+this.numeroDelicence;
    }
}