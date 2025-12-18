public class Solution 
{
    public static int totalMoney(int n)
    {
        int m = n/7;
        int r = n%7;
        return (m * 28) + 7 * ((m) * (m-1)/2) + (r * (r+1)/2) + (r * m);
    }
    public static void main(String[] args) 
    {
        int n = 10;
        System.out.println(totalMoney(n));
    }
}
