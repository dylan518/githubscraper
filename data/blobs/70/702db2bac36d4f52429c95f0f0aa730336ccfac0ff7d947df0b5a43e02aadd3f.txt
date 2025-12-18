package array;

public class RichestCostumerWealth {
    public static void main(String[] args) {
        RichestCostumerWealth rCW = new RichestCostumerWealth();
        int[][] accounts = {{2, 8, 7}, {7, 1, 3}, {1, 9, 5}};
        System.out.println(rCW.maximumWealth(accounts));
    }

    public int maximumWealth(int[][] accounts) {
        int[] max = new int[accounts.length];
        int max2 = 0;
        for (int i = 0; i < accounts.length; i++) {
            for (int j = 0; j < accounts[i].length; j++) {
                max[i] += accounts[i][j];
            }
        }
        for (int i = 0; i < max.length; i++) {
            for (int j = 0; j < max.length; j++) {
                max2 = max[i];
                if (max2 < max[j]) {
                    max2 = max[j];
                    break;
                }
            }
            if (max2 == max[i]) {
                return max2;
            }
        }
        return max2;
    }
}
