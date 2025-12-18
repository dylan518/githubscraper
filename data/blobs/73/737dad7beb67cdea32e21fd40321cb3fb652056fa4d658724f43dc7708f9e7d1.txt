import java.io.*;
import java.util.*;

/* 규영이와 인영이의 카드게임
1~18
 */

public class Solution {

    static boolean isSelected[];
    static int[] K_cards, I_cards, permutation;
    static int count;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            boolean[] card = new boolean[19]; // card 1~18
            K_cards = new int[9];
            I_cards = new int[9];
            permutation = new int[9];
            isSelected = new boolean[9];
            count = 0;

            for (int i = 0; i < 9; i++) {
                K_cards[i] = sc.nextInt();
                card[K_cards[i]] = true; // 규영이 카드 true로 체크
            }


            int idx = 0;
            for (int i = 1; i <= 18; i++) {
                if (!card[i]) {  // 규영이 카드가 아닌 숫자를
                    I_cards[idx++] = i; // 인영이 카드 배열에 저장
                }
            }

            makePermutation(0);

            System.out.println("#" + test_case + " " + count + " " + (362880 - count));

        }
    }

    static void makePermutation(int cnt) {
        if (cnt == 9) { // 순열이 완성됐을 때,
            int K_score = 0, I_score = 0;
            for (int i = 0; i < 9; i++) {   // 규영과 인영의 카드들 비교
                if (K_cards[i] > permutation[i]) {
                    K_score += K_cards[i] + permutation[i];
                } else if (K_cards[i] < permutation[i]) {
                    I_score += K_cards[i] + permutation[i];
                }
            }
            if (K_score > I_score)
                count++;
        } else {
            for (int i = 0; i < 9; i++) {
                if (isSelected[i]) continue;

                permutation[cnt] = I_cards[i];  // [cnt]에 저장! 자리는 계속 바뀐다

                isSelected[i] = true;
                makePermutation(cnt + 1);
                isSelected[i] = false;
            }
        }
    }


}
