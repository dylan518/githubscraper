import java.util.Scanner;

public class Parameters {

    public static Scanner scanner = new Scanner(System.in);

    public static void calculateArea(double length, double width){
        double area = length * width;
       System.out.println("Area: "+ area);
       
    }

    
    
    public static void main(String[] args) {
        
        calculateArea(1,2);
        calculateArea(3,2);



    scanner.close();
    }
    
}
