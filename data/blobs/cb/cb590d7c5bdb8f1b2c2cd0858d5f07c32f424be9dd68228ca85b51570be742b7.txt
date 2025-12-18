package StacksAndQueues;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Scanner;

public class P04MatchingBrackets {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

//        1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
        String input = scanner.nextLine();
        char[] inputCharArray = input.toCharArray();
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int index = 0; index < inputCharArray.length; index++) {

            switch (inputCharArray[index]) {

                case '(':
                    stack.push(index);
                    break;

                case ')':
                    int startIndex = stack.pop();
                    String contents = input.substring(startIndex, index + 1);
                    System.out.println(contents);
                    break;
            }
        }

    }
}
