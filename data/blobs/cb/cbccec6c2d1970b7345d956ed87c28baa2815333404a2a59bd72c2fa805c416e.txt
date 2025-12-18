// TestaTributavel.java
public class Main {
    public static void main(String[] args) {
        // Criando instâncias de ContaCorrente, ContaPoupanca e SeguroDeVida
        ContaCorrente contaCorrente = new ContaCorrente(1000.0);
        ContaPoupanca contaPoupanca = new ContaPoupanca(500.0);
        SeguroDeVida seguroDeVida = new SeguroDeVida();

        // Calculando e exibindo os tributos
        double tributosContaCorrente = contaCorrente.calculaTributos();
        double tributosSeguroDeVida = seguroDeVida.calculaTributos();

        System.out.println("Tributos da Conta Corrente: " + tributosContaCorrente + " reais");
        System.out.println("Tributos do Seguro de Vida: " + tributosSeguroDeVida + " reais");
    }
}
