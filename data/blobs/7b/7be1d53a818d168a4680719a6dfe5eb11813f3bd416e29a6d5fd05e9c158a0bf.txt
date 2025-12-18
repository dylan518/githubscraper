
/*
 * Crear un algoritmo que muestre cada uno de los dígitos de un número ingresado por el usuario. El máximo permitido es de 4 dígitos. Al final debe mostrar la suma de los dígitos. Por ejemplo: si se ingresa el número 187, entonces debe mostrar en un único cartel lo siguiente: “d1 = 0, d2 = 1, d3 = 8 y d4 =7. suma= 16”.
 * 
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Ex6{
    static BufferedReader cnsl = new BufferedReader(new InputStreamReader(System.in));
    static int number = 0, size = 4;
    static int[] separated = {0, 0, 0, 0};
    
public static void main(String []args) {        //main 
    ask4number();
    separatenumber(number);
    printnumber(separated);
}

static void ask4number(){
    
    try{  
        System.out.println("Please enter a number (Up to 4 digits). " );
        number = Integer.parseInt(cnsl.readLine());
    } 
    catch (Exception e){  
        System.out.println("Please enter a number. " ); //requests digits
    }
}

static void separatenumber(int num){
    
    try{
        // for (int i = 0; i < size; i++){
        //     separated[i] = num / (1000/(10^(i)));
        //     num -= separated[i]; 
        // }  


        separated[0] = num / 1000;
        num -= separated[0];
        separated[1] = num / 100;
        num -= separated[1];
        separated[2] = num / 10;
        num -= separated[2];
        separated[3] = num / 1;
    } 
    catch (Exception e){  
        
    }
}

static void printnumber(int[] array){
    
    try{    
        
        for (int i = 0; i < size; i++){
            System.out.println("d" +(i+1)+": "+ array[i] ); //requests digits
        }  
    } 
    catch (Exception e){  
        
    }
}

}