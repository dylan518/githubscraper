package Voorbeelden.Opdracht8;

public class Figuren {
    public static void main(String[] args) {
        Cirkel cirkel1 = new Cirkel(10, 20, 50);
        Cirkel cirkel2 = new Cirkel(1, 5, 20);
        System.out.printf("Cirkel1 omtrek: %.2f opp: %.2f%n", cirkel1.getOmtrek(), cirkel1.getOppervlakte());
        System.out.printf("Cirkel2 omtrek: %.2f opp: %.2f%n", cirkel2.getOmtrek(), cirkel2.getOppervlakte());
    }
}
