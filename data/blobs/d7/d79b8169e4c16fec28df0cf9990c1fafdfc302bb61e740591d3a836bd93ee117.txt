package programmers2;

public class NextBiggerNumber {

	//프로그래머스 Level 2. 다음 큰 숫자
	//https://school.programmers.co.kr/learn/courses/30/lessons/12911
	public static void main(String[] args) {
		NextBiggerNumber nbn = new NextBiggerNumber();
		
		int n1 = 78;
		System.out.println(nbn.solution(n1));
		
		int n2 = 15;
		System.out.println(nbn.solution(n2));
	}
	
    public int solution(int n) {
    	int cntOne = Integer.bitCount(n);
    	while(true) {
    		n++;
    		if(cntOne == Integer.bitCount(n)) break;
    	}
        return n;
    }

}
