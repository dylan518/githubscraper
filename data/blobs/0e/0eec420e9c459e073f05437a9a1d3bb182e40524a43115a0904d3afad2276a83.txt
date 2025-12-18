package com.sanedge.interview.backtracking;

public class WordSearch {

    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (
                    board[r][c] == word.charAt(0) && dfs(board, r, c, word, 0)
                ) {
                    return true;
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, int r, int c, String word, int index) {
        if (index == word.length()) {
            return true;
        }

        if (
            r < 0 ||
            r >= board.length ||
            c < 0 ||
            c >= board[0].length ||
            board[r][c] != word.charAt(index)
        ) {
            return false;
        }

        char temp = board[r][c];
        board[r][c] = '#';

        int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

        for (int[] dir : directions) {
            int newR = r + dir[0];
            int newC = c + dir[1];

            if (dfs(board, newR, newC, word, index + 1)) {
                return true;
            }
        }

        board[r][c] = temp;

        return false;
    }
}
