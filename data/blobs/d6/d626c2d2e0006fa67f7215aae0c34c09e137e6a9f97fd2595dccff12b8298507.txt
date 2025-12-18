
import Materia.Controller.MenuController;
import Materia.Stacks.StackGeneric;
import Materia.Stacks.Stacks;

import java.util.Scanner;

import Ejercicio_01_sign.ValidacionSign;
import Ejercicio_02_sorting.OrdenarStack;

public class App {
    public static void main(String[] args) throws Exception {
        //runStack();
        //runContactMannager();
        Validador();
        OrdenarStack();
    }
    public static void runStack(){
        
        Stacks stack = new Stacks();

        stack.push(5);
        stack.push(7);
        stack.push(10);
        stack.push(20);

        stack.printStack();
        System.out.println("Tamano: "+stack.getSize());

        System.out.println("Cima: "+stack.peek());
        System.out.println("Retirar: "+stack.pop());
        System.out.println("Cima: "+stack.peek());
        System.out.println("Retirar: "+stack.pop());
        System.out.println("Cima: "+stack.peek());


    }

    public static void runContactMannager(){
        MenuController menucontroller = new MenuController();
        menucontroller.showMenu();
    }

     private static void Validador() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese los signos signos: ");
        String input = scanner.nextLine();
        System.out.println("La validación es: " + ValidacionSign.esValido(input));
        
    }
    private static void OrdenarStack() {
        Scanner scanner = new Scanner(System.in);
        StackGeneric<Integer> stack = new StackGeneric<>();
        System.out.println("Ingrese los numeros ('X' para salir):");
        
        while (true) {
            //System.out.println("");
            String input = scanner.next();
            if (input.equalsIgnoreCase("X")) {
                break;
            }
            try {
                stack.push(Integer.parseInt(input));
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un número válido.");
            }
        }
        
        System.out.println("Stack sin ordenar: " + stack);
        OrdenarStack.ordenar(stack); 
        System.out.println("Stack ordenado: " + stack);
        scanner.close();
    }
      

}
