package 스택의활용;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class p3986 {
    /**
     * 나의 풀이 방법: 처음엔 다른 방법으로 이전 문자열과 다르면 false로 두고 그 다음 문자열을 확인 하는
     * 방법을 사용했다. 근데 내가 했던 로직으로는 false + 다른 문자열이면 (ex BAB) 로직이 종료된다.
     * 그러나 BABBAB 경우 뒤에 문자열을 통해 상쇄가 가능하다. 그래서 간단하게 기본 스택 방식으로
     * 문제를 풀었더니 풀렸다.
     *
     */
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        int answer =0;

        for (int i = 0; i < n; i++) {
            String input = bf.readLine();
            Stack<Character> stack = new Stack<>();

            boolean flag = true;

            if(input.length() % 2 != 0) continue;

            for (int k = 0; k < input.length(); k++) {
                if (stack.isEmpty()) {
                    stack.push(input.charAt(k));
                } else {
                    if(stack.peek() == input.charAt(k)) stack.pop();
                    else stack.push(input.charAt(k));
                }
            }

            if(!stack.isEmpty()) flag = false;

            if(flag) answer++;

        }

        System.out.println(answer);
    }
}
