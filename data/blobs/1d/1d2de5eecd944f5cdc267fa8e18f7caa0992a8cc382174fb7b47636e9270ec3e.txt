/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package algotithms;
import java.util.Scanner;
/**
 *
 * @author user
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sort[] = new int[5];
        
        
        for(int i=0;i<sort.length;i++){
            System.out.print("Enter Number "+(i+1)+" :");
            sort[i] = sc.nextInt();
        }
        
       BubbleSort Sort = new BubbleSort();
        System.out.print("\nBubble Sort Assending Order:");
       Sort.assending(sort);
     
        System.out.print("\nBubble Sort Descending Order:");
        Sort.dessending(sort);
        System.out.println("\n");
      
       
    }
    
    
}
