package Programmers;

//부족한 금액 계산하기
public class Q12 {
    public static void main(String[] args) {
        Q12 sol1 = new Q12();
        System.out.println(sol1.solution(3,20,4));
    }
    public long solution(int price, int money, int count) {
        long need = 0;

        for (int i = 0; i < count; i++) {
            need += price * (i+1);
        }
        if (money - need >= 0) {
            return 0;
        }
        else {
            return need - money;
        }
    }
}
