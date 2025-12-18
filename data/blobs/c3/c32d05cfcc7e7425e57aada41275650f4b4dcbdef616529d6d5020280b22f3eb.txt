public class Solution 
{
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) 
    {
        int count=0;   
        while(n!=0)
        {
            //check if the last bit is 1 or not
            if((n&1)==1) //if it is 1
            {
                count++;
            }
            //simply right shift the number by 1..
            //for unsigned right shift (use this ">>>")
            n = n>>>1;
        }
        return count; 
    }
}
