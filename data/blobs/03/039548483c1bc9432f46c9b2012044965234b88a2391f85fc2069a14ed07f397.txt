import model.Produto;

public class Main {
    public static void main(String[] args) {

        System.out.println("Hello, World!");

        Produto p = new Produto("Tv", 2500, 0.034324324);

        double precoFInalDaTV = p.calcularPrecoFinal();

        String x = String.format( "%.2f", precoFInalDaTV );
        System.out.println(
                "O preco da tv 'e " +  x
        );


    }
}