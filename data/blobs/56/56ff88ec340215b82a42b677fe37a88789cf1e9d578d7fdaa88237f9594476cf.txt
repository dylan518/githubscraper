public class largest 
{
    public static int max(int a[])
    {
        int max=Integer.MIN_VALUE;
        for(int i=0;i<a.length;i++)
        {
            if(a[i]>max) max=a[i];
        }
        return max;
    }
    public static void main(String[] args) 
    {
        int a[]={34,56,23,8,45,32};
        System.out.println("The largest element is:"+max(a)); 
    }
}
