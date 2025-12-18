//Oppgave 1F

// importer inn pakken for å bruke klassen ArrayList
import java.util.ArrayList;

public class Konto{
  
  //Privat datafelt
  //bruker Arraylist pga den er dynamisk
  private int kontoNummer;
  private double saldo;
  private double rente;
  private double akkumulertRente;
  private ArrayList <Transaksjon> transaksjonsListe = new ArrayList<>();
  private Dato dato = new Dato();
  
  //Konstruktør
  Konto(int kontoNummer, double rente){
    this.kontoNummer = kontoNummer;
    this.rente = rente;
    this.saldo = 0.0;
    this.akkumulertRente = 0.0;
  }
  
  // lager getter metoder siden data feltet er privat. Vi vil ikke endre kontoNummer, saldo. 
  public int hentKontoNummer(){
    return kontoNummer;
  }
  
  public double hentSaldo(){
    return saldo;
  }
  
  public double hentRente(){
    return rente;
  }
  
  public void setRente(double rente){
    this.rente = rente;
  }
  
  public double hentAkkumulertRente(){
    return akkumulertRente;
  }
  
  ////////////////////////////////////////////////////////////////////////////////////////////  
  
  // Oppgave 1 G
  
  public void utforTransaksjon(double belop, String tekst) throws IkkeDekningException{
    
      if ( (saldo + belop) < 0){
        // kaster nytt unntak 
        throw new IkkeDekningException("ERROR! Ikke nok penger.");
      }
      
      else{
        // oppdaterer saldoen
        saldo += belop;
        // leger til ny trasaksjon til listen
        transaksjonsListe.add(new Transaksjon(belop, tekst));
        System.out.println("Transaksjon fullført!");
        System.out.println("Saldo: "+saldo);
      }
    }
    
  ////////////////////////////////////////////////////////////////////////////////////////////  
  // Oppgave 1 H
  public void innSkudd(double belop) throws IkkeMuligMedNegativtBelopException, IkkeDekningException{
    if (belop < 0) {
      throw new IkkeMuligMedNegativtBelopException("ERROR! Ikke lov med negativt belop.");
    }
    
    else {
      // kaller på funksjonen og legger til belopet med melding innskudd
      utforTransaksjon(belop, "innskudd");
      System.out.println("Innskudd fullførst!");
      System.out.println("Saldo: "+saldo);
    }
  }
  
   ////////////////////////////////////////////////////////////////////////////////////////////  
  // Oppgave 1 Anatar at det er skrive feil i oppgaven.
  // står at jeg skal kalle gebyr metoden antar at det skulle stå kalles fra uttak metoden.
  
  public void uttak(double belop) throws IkkeMuligMedNegativtBelopException, IkkeDekningException{
    if (belop < 0) {
      throw new IkkeMuligMedNegativtBelopException("ERROR! Ikke lov med negativt belop.");
    }
    
    else {
      // kaller på funksjonen og trekker fra belopet med melding innskudd
      // ganger med -1 siden vi skal trekke fra saldo
      utforTransaksjon( -1 * belop, "uttak");
      System.out.println("Uttak fullførst!");
      System.out.println("Saldo: "+saldo);
    }
  }
  
   ////////////////////////////////////////////////////////////////////////////////////////////  
  // Oppgave 1 j
  
  public void gebyr(double belop) throws IkkeMuligMedNegativtBelopException, IkkeDekningException{
    if (belop < 0) {
      throw new IkkeMuligMedNegativtBelopException("ERROR! Ikke lov med negativt belop.");
    }
    
    else {
      // kaller på funksjonen og trekker fra belopet med melding innskudd
      // ganger med -1 antar at denn funksjonen skal trekke fra saldo
      utforTransaksjon( -1* belop, "gebyr");
      System.out.println("Gebyr fullført!");
      System.out.println("Saldo: "+saldo);
    }
  }
  
  public void beregnRenter(){
    
    // beregner den dalige renten
    double dagligRente = rente / 365;
    akkumulertRente += (saldo * dagligRente);
    
    Dato datoSammenlign = new Dato();
    
    // dersom maaned ikke er like etter ny kjoring
    if (dato.hentMaaned() != datoSammenlign.hentMaaned()){
      // antar at det er banken som tjener den akkumulertRenten
      
      // setter akkumulertRente lik 0
      akkumulertRente = 0.0;
      
      // oppdaterer dato objektet
      dato.oppdaterDato();
    }
  }
  
  public String toString(){
    return "Kundenummer: " +kontoNummer+ " saldo: "+saldo;
  }
}













