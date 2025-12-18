public class Maxi_Product {
	public static int Maxii(int[] arr, int n) {
		int maxi = 0;
		int sec_max = 0;
		for (int num : arr) {
			if (num > maxi) {
				sec_max = maxi;
				maxi = num;
			} else {
				sec_max = Math.max(sec_max, num);
			}
		}
		return (maxi - 1) * (sec_max - 1);
	}

	public static void main(String[] args) {
		int arr[] = { 1, 5, 4, 5 };
		int n = arr.length;
		int ans = Maxii(arr, n);
		System.out.print(ans);
	}
}