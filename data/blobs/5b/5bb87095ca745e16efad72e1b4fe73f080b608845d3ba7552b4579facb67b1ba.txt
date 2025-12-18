public class PrimeinRange {
    public static void main(String args[]){

isPrimeRange(100);


    }

    public static void isPrimeRange(int n){


        for(int i=2;i<=n;i++){
            if(isPrime(i)){
                System.out.print(i+ " ");
            }
        }
        System.out.println();

        
    } 

    public static boolean isPrime(int n){

        boolean isPrime=true;


        if(n==2){
            isPrime=true;
        }
        else{

for(int i=2;i<=Math.sqrt(n);i++){

            if(n%i==0){
                isPrime=false;
                break;
            }
        }


        }
return isPrime;
        

    }

}
