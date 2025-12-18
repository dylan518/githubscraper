import java.util.Scanner;

public class 백준5_10 {
    
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String a = s.nextLine();
        char[] arr = a.toCharArray();

        int time = 0;

        for (int i = 0; i<arr.length; i++) {
            int b = arr[i];

            if (b == 'A'|| b == 'B' || b == 'C' ) {
                time+=3;
            }else if (b == 'D'||b == 'E'||b == 'F'){
                time+=4;
            }else if (b == 'G'||b == 'H'|| b == 'I') {
                time+=5;
            }else if (b == 'J'||b == 'K'|| b == 'L') {
                time+=6;
            }else if (b == 'M'||b == 'N'|| b == 'O') {
                time+=7;
            }else if (b == 'P'||b == 'Q'|| b == 'R'||b == 'S') {
                time+=8;
            }else if (b == 'T'||b == 'U'|| b == 'V') {
                time+=9;
            }else {
                time+=10;
            }
            
        }
        System.out.println(time);
        s.close();
    }
}
