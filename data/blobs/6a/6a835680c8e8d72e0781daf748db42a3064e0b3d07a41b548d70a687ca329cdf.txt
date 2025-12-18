class GridWays {
    public static int gridWays(int i, int j, int n, int m) {
        //base case
        if (i == n - 1 && j == m - 1) {
            return 1;
        } else if (i > n || j > m) {
            return 0;
        }

        //kaam
        int w1 = gridWays(i + 1, j, n, m);
        int w2 = gridWays(i, j + 1, n, m);
        return w1 + w2;
    }

    public static int factorial(int n) {
        if (n == 1 || n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    
    public static int linearTimeGridWays(int n, int m) {
        return factorial(n-1 + m -1) / (factorial(n - 1) * factorial(m - 1));
    }

    public static void main(String[] args) {
        int m = 3, n = 3;
        System.out.println(gridWays(0, 0, n, n));
       System.out.println(linearTimeGridWays(n, m));
   } 
}
