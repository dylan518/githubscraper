//Algorithim does not currently work if the digram has repeated letters

import java.util.*;
import java.util.stream.Collectors;

public class playfair{
    public static void main(String[] args){
       Scanner scanner = new Scanner(System.in);
       System.out.println("Enter Keyword");
       String keyword = scanner.next();
       keyword = keyword.toLowerCase();
       keyword = keyword.trim();
       List<Character> chars = new ArrayList<Character>();
       for(int i=0;i<keyword.length();i++){
        chars.add(keyword.charAt(i));
       }
       chars = chars.stream().distinct().collect(Collectors.toList());
       char matrix[][] = new char[5][5];
       generateTable(matrix, chars);
       List<String> digrams1 = new ArrayList<String>();
       System.out.println("Enter text to be encrypted");
       String plaintext = scanner.next();
       generateDigrams(plaintext, digrams1);
       String cipher = encryption(digrams1,matrix);
       System.out.println(cipher);
       List<String> digrams2 = new ArrayList<String>();
       generateDigrams(cipher, digrams2);
       String original = encryption(digrams2, matrix);
       System.out.println(original); 
    }
    public static void generateTable(char matrix[][],List<Character> chars){
        int j = 0;
        int k = 0;
        for(int i =0;i<chars.size();i++){
            matrix[j][k] = chars.get(i);
            if(k == 4){
                k = 0;
                j++;
            }
            else{
                k++;
            }
        }
        int i =0;
        char[] alphabet = {'a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        for(;i<25;i++){
        while(chars.contains(alphabet[i])){
                    i++;
        }
        matrix[j][k] = alphabet[i];
        if(k == 4){
            k = 0;
            j++;
        }
        else{
            k++;
        }
    }
  }
 
  public static void generateDigrams(String plaintext,List<String> digrams){
    if(plaintext.length() % 2 == 0){
        for(int i =0 ;i<plaintext.length() - 1;i = i + 2){
            digrams.add(Character.toString(plaintext.charAt(i)) + Character.toString(plaintext.charAt(i+1)));
        }
    }
    else{
        for(int i =0;i<plaintext.length();i = i+2){
            if(i == plaintext.length() -1){
               digrams.add(Character.toString(plaintext.charAt(i)) + Character.toString('x'));
               break;
            }
            digrams.add(Character.toString(plaintext.charAt(i)) + Character.toString(plaintext.charAt(i)));
        }
    }
  }

  public static String encryption(List<String> digrams,char matrix[][]){
    String ciphertext = "";
    int r1 = 0;
    int r2 = 0;
    int c1 = 0;
    int c2 = 0;
    for(int i = 0;i<digrams.size();i++){
        for(int j =0;j<5;j++){
            for(int k =0;k<5;k++){
                if(digrams.get(i).charAt(0) == matrix[j][k]){
                    r1 = j;
                    c1 = k;
                    break;
                }
            }
        }
        for(int j =0;j<5;j++){
            for(int k =0;k<5;k++){
                if(digrams.get(i).charAt(1) == matrix[j][k]){
                    r2 = j;
                    c2 = k;
                    break;
                }
            }
        }
    if(r1 == r2){
        ciphertext += Character.toString(matrix[r1][(c1 +1)%5]) + Character.toString(matrix[r2][(c2 +1)%5]);
    }
    else if(c1 == c2){
        ciphertext += Character.toString(matrix[(r1+1)%5][c1]) + Character.toString(matrix[(r2+1)%5][c2]);
    }
    else{
        ciphertext += Character.toString(matrix[r1][c2]) + Character.toString(matrix[r2][c1]);
    }
  }
return ciphertext;
 }
}