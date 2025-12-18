import java.util.Scanner;

public class To_find_pairs { 
    public static void main(String[] args) {
        //program to find the pairs of number in our array 
        int number;  
        int arr[]={1,2,3,4,5,6,7,8,9,10};
        System.out.println("Enter the number"); 
        Scanner sc = new Scanner(System.in); 
        number=sc.nextInt();  
         pairs(arr,number);  
         sc.close();  
    } //int arr[], int number
     static void pairs(int arr[], int number){ 
        
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]+arr[j]==number){
                    System.out.println("pairs are following");
                    System.out.println(arr[i]+"+"+arr[j]+"="+number);
                }
            }
        }
    }
   
}
