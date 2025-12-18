package loop;

public class Continue1_1 {
    public static void main(String[] args) {
        int i = 1;

        while (i <= 5) {
            if (i == 3) {
                i++;
                continue;   // 출력을 건너띄고 다시 조건문으로 이동 -> 하단 출력안함
            }
            System.out.println(i);
            i++;
        }
    }
}
