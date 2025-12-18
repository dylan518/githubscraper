package mar;

public class Solution230318_4 {
	
	// 프로그래머스 - lv.1 - 짝수와 홀수
	
	public String solution(int num) {
        String answer = "";
        
        answer = num % 2 == 0 ? "Even" : "Odd";
        
        return answer;
    }
	
	public static void main(String[] args) {
		Solution230318_4 s = new Solution230318_4();
		String result = s.solution(3);
		
		System.out.println(result);
	}
	
}
