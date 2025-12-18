package Telefone;

public class AparelhoTelefonico {
    private String numero;

    public AparelhoTelefonico(String numero) {
        this.numero = numero;
    }

    public void ligar() {
        System.out.println("Ligando para " + numero);
    }

    public void atender() {
        System.out.println("Atendendo chamada de " + numero);
    }

    public void iniciarCorreioVoz() {
        System.out.println("Iniciando correio de voz");
    }
}