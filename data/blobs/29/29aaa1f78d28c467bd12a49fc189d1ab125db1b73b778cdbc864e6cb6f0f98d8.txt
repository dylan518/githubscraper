import java.util.Scanner;

public class Salario1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Qual valor do salário bruto:");
        double salarioBruto= scanner.nextDouble();

        System.out.println("Qual valor dos beneficios:");
        double beneficios = scanner.nextDouble();
        double valorImposto = 0;

        if(salarioBruto <= 0){
            System.out.println("Digite um sálario.");
        }
        else if(salarioBruto > 0 && salarioBruto <= 1100.00){
            valorImposto = 0.05 * salarioBruto;
        }
        else if(salarioBruto > 1100.00 && salarioBruto <= 2500.00){
            valorImposto = 0.10 * salarioBruto;
        }
        else if(salarioBruto > 2500.00) {
            valorImposto = 0.15 * salarioBruto;
        }

        double resultado = salarioBruto - valorImposto + beneficios;
        System.out.println("O sálario transferido para o funcionário foi de: " + resultado);
        
    }
}
