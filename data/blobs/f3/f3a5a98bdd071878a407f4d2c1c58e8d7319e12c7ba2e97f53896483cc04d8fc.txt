package src.com.leetcode.isValid;

import java.util.Deque;
import java.util.LinkedList;

public class IsValid {
  public static void main(String[] args) {
    boolean valid = isValid("()");
    System.out.println(valid);

  }

  public static boolean isValid(String s) {
    Deque<Character> stack = new LinkedList<Character>();
    for (char c : s.toCharArray()) {
      if (c == '(') {
        stack.push(')');
      } else if (c == '{') {
        stack.push('}');
      } else if (c == '[') {
        stack.push(']');
      } else if (stack.isEmpty() || stack.pop() != c) {
        return false;
      }
    }
    return stack.isEmpty();
  }
}
