package pkg1205henger;



public class TomorHenger extends Henger{
    
    private double fajsuly;

    public TomorHenger(double fajsuly, double sugar, double magassag) {
        super(sugar, magassag);
        this.fajsuly = fajsuly;
        
        //this(sugar,magassag); -- rekurziv hívás, nem fog lefordulni
    }

    public TomorHenger(double sugar, double magassag) {
        super(sugar, magassag);
    }
    

    public void setFajsuly(double fajsuly) {
        this.fajsuly = fajsuly;
    }

    

    public double getFajsuly() {
        return fajsuly;
    }
    
    public double suly(){
        return super.terfogat() * fajsuly;
    }

    @Override
    public String toString() {
        String os = super.toString();
        return os + "\n\t" + "Tömörhenger{"+"Fajsúly="+fajsuly;
        //return "TomorHenger{" + "fajsuly=" + fajsuly + '}';
    }

    
    
    
}
