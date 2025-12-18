import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String s = new Scanner(System.in).nextLine();
        StringBuilder output = countingSort(s);

        System.out.println(output);

        System.out.println(output.reverse());
    }

    public static StringBuilder countingSort(String s){
        int[] t = new int[26];
        for (int i = 0; i < s.length(); i++) {
            t[s.charAt(i) - 97]++;
        }

        StringBuilder st = new StringBuilder();
        for(int i = 0; i < t.length; i++) {
            while (t[i] > 0){
                st.append((char) (i + 97));
                t[i]--;
            }
        }

        return st;
    }
}