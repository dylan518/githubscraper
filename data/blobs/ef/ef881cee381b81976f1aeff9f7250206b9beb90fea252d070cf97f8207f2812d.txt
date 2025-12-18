package stack.problem_3;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[][] board = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                board[i][j] = scanner.nextInt();
            }
        }

        int M = scanner.nextInt();
        int[] moves = new int[M];
        for (int i = 0; i < M; i++) {
            moves[i] = scanner.nextInt();
        }
        int result = main.solution(N, board, M, moves);
        System.out.println(result);
    }

    public int solution(int N, int[][] board, int M, int[] moves) {
        int result = 0;
        Stack<Integer> resultBasket = new Stack<>();

        ArrayList<Stack> boardColumns = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            Stack<Integer> stack = new Stack<>();

            for (int j = N - 1; j >= 0; j--) {
                int target = board[j][i];
                if (target != 0) stack.push(target);
            }

            boardColumns.add(stack);
        }


        for (int move : moves) {
            int idx = move - 1;
            Stack<Integer> column = boardColumns.get(idx);

            if (column.isEmpty()) continue;

            int pickedElement = column.pop();
            int lastElementInBasket = peekOrDefault(resultBasket);

            if (pickedElement == lastElementInBasket) {
                resultBasket.pop();
                result += 2;
            } else {
                resultBasket.push(pickedElement);
            }
        }

        return result;
    }

    private int peekOrDefault(Stack<Integer> stack) {
        try {
            return stack.peek();
        } catch (Exception err) {
            return -1;
        }
    }
}
