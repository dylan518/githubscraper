/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modell;

/**
 *
 * @author ViczaiPéterMilán(SZO
 */
public class Csigusz {
    
    public enum Szinek{PIROS, ZOLD, KEK};
    
    private static final String RESET = "\u001B[0m";
    private static final String RED = "\u001B[31m";
    private static final String GREEN = "\u001B[32m";
    private static final String BLUE = "\u001B[34m";
    
    private String nev;
    //private String szinNev;
    private Szinek szinNev;
    private String szinKod;

    public Csigusz(String nev) throws Exception {
        //this(nev, "piros");
        this(nev, Szinek.PIROS);
        //this.nev = nev;
        //this.szin = "fekete";
    }

    //public Csigusz(String nev, String szinNev) throws Exception {
    public Csigusz(String nev, Szinek szinNev) throws Exception {
        setNev(nev);
        //this.szinNev = szinNev;
        this.szinKod = RESET;
        this.szinNev = szinNev;
        setSzin();
        
        
    }

//    public Csigusz() throws Exception {
        //this("Csigusz Doe", "fekete");
//        this("Csigusz Doe");
//    }

    public void setNev(String nev) throws Exception {
        if (nev.length() >= 3) {
            char nevElso = nev.charAt(0);
            if (Character.isLowerCase(nevElso)) {
                nevElso = Character.toUpperCase(nevElso);
                nev = nevElso + nev.substring(1);
            }
            
            this.nev = nev;
        } else {
            throw new Exception("A név túl rövid");
        }
    }
    
    
    

    public String getNev() {
        return nev;
    }

    public String getSzin() {
        return szinNev.toString();
    }
    
    private void setSzin() {
        switch(szinNev) {
            //case "piros":
            case PIROS:
                szinKod = Csigusz.RED;
                break;
            //case "kék":
            case KEK:
                szinKod = Csigusz.BLUE;
                break;
            //case "zöld":
            case ZOLD:
                szinKod = Csigusz.GREEN;
                break;
        }
    }
    
    

    @Override
    public String toString() {
        return szinKod + "Csigusz{" + "nev=" + nev + ", szin=" + szinNev + '}' + RESET;
    }
    
    
    
}
