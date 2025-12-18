package Arrays;

public class PalindromeCount {

    public static void main(String[] args) {
        String[] words ={"anna", "level", "Java"};

        int palindromeCount =0;

        for(String word : words){
            if(new StringBuilder(word).reverse().toString().equals(word)){
                palindromeCount++;

            }
        }
        System.out.println("number of palindromes:" + palindromeCount);
    }
}
