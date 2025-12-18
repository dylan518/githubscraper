package stacksAndQueues;

import java.util.Stack;

public class PostfixToInfix {
    static String postToInfix(String exp) {
        Stack<String> stack = new Stack<>();
        for (char c : exp.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                stack.push(String.valueOf(c));
            } else {
                String b = stack.pop();
                String a = stack.pop();
                stack.push("(" + a + c + b + ")");
            }
        }
        return stack.pop();
    }

    public static void main(String[] args) {
        System.out.println(postToInfix("ab*c+"));
    }
}
