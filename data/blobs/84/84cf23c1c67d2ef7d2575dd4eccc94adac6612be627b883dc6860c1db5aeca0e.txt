public class qsn {
    public static void main(String[] args) {
        int n = 34;
        boolean[] arr = primeSieve(n);
        int a=0;
        for(int i=0;i<n;i++){
            if(arr[i]==false && arr[n-i]==false){
                System.out.println("YES");
                a=1;
                break;
            }
        }
        if(a==0){
        System.out.println("NO");
        }
    }
    public static boolean[] primeSieve(int n){
        boolean[] prime= new boolean[n+1];
        for(int i=2;i*i<=n;i++){
            if(prime[i]==false){
                for(int j=i*i;j<=n;j+=i){
                    prime[j]=true;
                }
            }
        }
        return prime;
    }

}
