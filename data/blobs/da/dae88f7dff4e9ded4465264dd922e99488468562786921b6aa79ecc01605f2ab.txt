public class HumanEval_115 {
    /**
     * Calculate the maximum fill for a given grid with a specified capacity.
     *
     * @param grid A 2D array representing the grid.
     * @param capacity The maximum capacity of each cell in the grid.
     * @return The total max fill value.
     */
    public static int maxFill(double[][] grid, int capacity) {
        int rows = grid.length;
        int cols = grid[0].length;
        double sum;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sum = 0.0;
                // Assuming all elements in the array are non-negative
                for (double val : grid[i]) {
                    sum += val;
                }
                int maxFill = (int) Math.ceil(sum / capacity);
                // Since the total capacity is not necessarily integer, 
                // adjust maxFill to be 0 if it's less than 0
                maxFill = Math.max(maxFill, 0);
            }
        }

        return maxFill;
    }
}