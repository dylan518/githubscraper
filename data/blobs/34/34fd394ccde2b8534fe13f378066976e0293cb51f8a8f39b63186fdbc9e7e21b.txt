import java.util.Scanner;

//19. Faça um algoritmo que receba o raio e a altura de um cilindro e retorne o seu volume calculado 
//    de acordo com a seguinte fórmula: 
//    volume = 3.14 * raio2 * altura; Exemplo: raio = 10, altura = 15. Volume = 4710

public class Ex19 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Solicita o raio e a altura do usuário
        System.out.println("Digite o raio do cilindro:");
        double raio = scanner.nextDouble();
        
        System.out.println("Digite a altura do cilindro:");
        double altura = scanner.nextDouble();
        
        // Calcula o volume do cilindro
        double volume = calcularVolumeCilindro(raio, altura);
        
        // Exibe o volume do cilindro
        System.out.println("Volume do cilindro: " + volume);
        
        scanner.close();
    }
    
    public static double calcularVolumeCilindro(double raio, double altura) {
        // Calcula o volume do cilindro usando a fórmula fornecida
        double volume = 3.14 * raio * raio * altura;
        
        return volume;
    }
}


