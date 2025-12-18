import java.util.Scanner;

public class ControleSimplesDeSaques {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); 

        double limiteSaque = scanner.nextDouble(); 
                
        boolean continuar = true;
        while (continuar) {
            double saque = scanner.nextDouble(); 
            if (saque > limiteSaque){
                System.out.println("Limite diario de saque atingido. Transacoes encerradas.");
                continuar = false;
            }else if (saque == 0){
                System.out.print("Transacoes encerradas.");
                continuar = false;
            }else{
                limiteSaque = limiteSaque - saque;
                System.out.println("Saque realizado. Limite restante: " + limiteSaque);
            }
        }
        scanner.close(); 
    }
}
// javac ControleSimplesDeSaques.java
// java ControleSimplesDeSaques
// del ControleSimplesDeSaques.class