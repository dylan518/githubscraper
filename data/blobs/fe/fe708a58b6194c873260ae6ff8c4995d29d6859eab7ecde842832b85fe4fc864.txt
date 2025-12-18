/*
import java.util.Scanner;

class D2Array2 {
    public static void main(String[] args) {
        int arr[][] = new int[2][5];
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.println("Enter Element Index " + i + j + ": ");
                arr[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
*/


// wap to find unique element from the array
/*
class D2Array2{
    public static void main(String[] ares){
       int arr[] = {1,2,3,1,2,3,4,5,6,7,8,9};
       int fre[] = new int[10];
       for(int i=0;i<arr.length;i++){
        fre[arr[i]]++;
       } 
       System.out.println("Unique Element of the Array :");
       for(int i=0;i<fre.length;i++){
        if(fre[i]==1){
            System.out.print("\t"+i);
        }
       }
    }
}
*/

/*
import java.util.Scanner;

class D2Array2{
    public static void main(String[] ares){
        Scanner sc = new Scanner(System.in);
        int arr[][] = new int[3][3];
        int sum = 0;
        int r,c;
        for(r=0;r<3;r++){
            for(c=0;c<3;c++){
                System.out.println("Enter Element :" + r + c + " :");
                arr[r][c]=sc.nextInt();
                sum = sum + arr[r][c];
            }
        }
        System.out.println("Total Sum : " + sum);
    }
}
*/


import java.util.Scanner;

class D2Array2{
    public static void main(String[] ares){
        Scanner sc = new Scanner(System.in);
        int arr[][] = new int[3][3];
        int sum = 0;
        int r,c;
        for(r=0;r<3;r++){
            for(c=0;c<3;c++){
                System.out.println("Enter Element :" + r + c + " :");
                arr[r][c]=sc.nextInt();
            }
        }
        
        for(r=0;r<3;r++){
            sum=0;
            for(c=0;c<3;c++){
                System.out.print("\t"+arr[r][c]);
                sum=sum+arr[r][c];
            }
            System.out.println("\t"+sum);
        }
        int nums[]=new int[3];
        for(r=0;r<3;r++){
            sum=0;
            for(c=0;c<3;c++){
                sum=sum+arr[c][r];
            }
            nums[r]=sum;
            System.out.print("");
        }
        for(int i=0;i<3;i++){
            System.out.print("\t"+nums[i]);
        }
    }
}