package java_ex;

import java.util.ArrayList;

public class ex4 {
	//로또번호 7자리 생성하기
	
	public static void main(String[] args) {
		
		lotto lt = new lotto();
		lt.random();

	}

}
class lotto {
	ArrayList<Object> rnumber = new ArrayList<>();
	int bonusBall;
	int w = 0;
	int lottoNum;
	public void random() {
		
		while(rnumber.size() < 7) {
			lottoNum = (int) Math.ceil(Math.random()*46);
			
			if(!rnumber.contains(lottoNum)) {
				rnumber.add(lottoNum);
				if(rnumber.size() == 6) {
					bonusBall = (int) Math.ceil(Math.random()*46);	
					rnumber.add(bonusBall);
				}
			}
			w++;
		}
		System.out.printf("이번주 로또 번호 \n%s\n마지막 보너스 번호는 %d",rnumber,bonusBall);
	}
}