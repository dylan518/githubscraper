package level1;

public class MakePrimeNumber {

	public static void main(String[] args) {
		// 소수 만들기
		int[] nums = { 1, 2, 7, 6, 4 };
		System.out.println(solution(nums));
	}

	public static int solution(int[] nums) {
		int answer = 0;
		for (int i = 0; i < nums.length; i++) {
			for (int j = i + 1; j < nums.length; j++) {
				for (int k = j + 1; k < nums.length; k++) {
					answer += (isPrimeNumber(nums[i] + nums[j] + nums[k])) ? 1 : 0;
				}
			}
		}
		return answer;
	}

	public static boolean isPrimeNumber(int num) { // 소수 판별
		if (num % 2 == 0)
			return false;
		for (int j = 3; j <= Math.sqrt(num); j += 2) {
			if (num % j == 0)
				return false;
		}
		return true;
	}

}
