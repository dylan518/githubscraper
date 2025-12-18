class Solution {
    public int solution(String[] board) {
        int answer = 1;
        int o = 0;
        int x = 0;
        boolean tripleO = false;
        boolean tripleX = false;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i].charAt(j) == 'O') {
                    o++;
                    if (check(board, 'O', i, j)) tripleO = true;
                } else if (board[i].charAt(j) == 'X') {
                    x++;
                    if (check(board, 'X', i, j)) tripleX = true;
                }
            }
        }
        if (o != x && o != x + 1) answer = 0;
        if ((tripleO && o != x + 1) || (tripleX && o != x)) answer = 0;
        return answer;
    }
    
    boolean check(String[] board, char c, int x, int y) {
        if (x == 0) {
            if (board[x + 1].charAt(y) == c && board[x + 2].charAt(y) == c) return true;
        }
        if (y == 0) {
            if (board[x].charAt(y + 1) == c && board[x].charAt(y + 2) == c) return true;
        }
        if (x == 1 && y == 1) {
            if (board[x - 1].charAt(y - 1) == c && board[x + 1].charAt(y + 1) == c) return true;
            if (board[x + 1].charAt(y - 1) == c && board[x - 1].charAt(y + 1) == c) return true;
        }
        return false;
    }
}