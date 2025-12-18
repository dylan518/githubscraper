package Lab;

import java.util.Scanner;

public class P09GreaterOfTwoValues {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //The values can be of type int, char of String.
        String dataTypeInput = scanner.nextLine();


        switch (dataTypeInput){
            case "int":
                int firstNum = Integer.parseInt(scanner.nextLine());
                int secondNum = Integer.parseInt(scanner.nextLine());
                int result = getMax(firstNum, secondNum);

                break;
            case "char":
                char firstSymbol = scanner.nextLine().charAt(0);
                char secondSymbol = scanner.nextLine().charAt(0);
                getMax(firstSymbol, secondSymbol);

                break;
            case "string":
                String firstText = scanner.nextLine();
                String secondText = scanner.nextLine();
                getMax(firstText, secondText);

                break;
        }


    }


    public static int getMax(int firstNum, int secondNum){
        int result = 0;
        if (firstNum > secondNum){
            result = firstNum;
        } else {
            result = secondNum;
        }
        System.out.println(result);
        return result;
    }

    public static char getMax(char firstS, char secondS){
        char result;
        if (firstS > secondS){
            result = firstS;
        } else {
            result = secondS;
        }
        System.out.println(result);
        return result;
    }

    public static String getMax(String firstText, String secondText){
        String result = "";
        if (firstText.compareTo(secondText) >= 0){
            result += firstText;
        } else {
            result += secondText;
        }
        System.out.println(result);
        return result;
    }

}
