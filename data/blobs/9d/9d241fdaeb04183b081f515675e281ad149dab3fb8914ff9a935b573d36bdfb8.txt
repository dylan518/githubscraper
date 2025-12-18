import java.util.*;

class SuperParent_excep {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        int a[] = new int[0];
        try { // in a single try block we can write multiple catch blocks
            int y = 5 / sc.nextInt();
            System.out.println("Inside the try block");
        } 
        catch (ArrayIndexOutOfBoundsException e) {
            
             
            System.out.println("out of bound exception");// when ever we dont know the type of exception by using super
                                                         // parent called Exception it shows the type of exception we
                                                         // are getting
        }
    }
}
