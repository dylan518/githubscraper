package Tutoria_04;

public class Main {
 public static void main(String[] args) {
    Tickete ticket1 = new Tickete("Sergio Peña", "Bogotá.");
    Tickete ticket2 = new Tickete("Viviana Peña", "Soacha.");
    Tickete ticket3 = new Tickete("Estefani Peña", "Tunja.");

    //int ticketesVendidos = Tickete.contadorTicketes;
    System.out.println("Ticketes vendidos: "+ticket1.getContador());
    ticket1.imprimirTicket();
    ticket2.imprimirTicket();
    ticket3.imprimirTicket();
 }
}
