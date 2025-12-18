package 중복없는로또생성2;

import java.util.ArrayList;

public class LottoEx2 {
    public static void main(String[] args) {
        ArrayList<Integer> lotto = new ArrayList<>();
        int tmp;
        while (true) {
            tmp = (int) (Math.random() * 45) + 1;
            if(!lotto.contains(tmp)) lotto.add(tmp);
            if(lotto.size() == 6) break;
        }
        for(int i = 0; i <lotto.size(); i++){
            System.out.print(lotto.get(i) + " ");
        }
    }
}
