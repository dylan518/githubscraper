import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        int num = sc.nextInt();

        if(num <= word.length()){
            for(int i = 1; i <= num; i++){
                System.out.print(word.charAt(word.length()-i));
            }
        }else{
            for(int i = 1; i <= word.length(); i++){
                System.out.print(word.charAt(word.length()-i));
            }
        }
    }
}