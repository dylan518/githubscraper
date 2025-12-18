package arrays;

public class Prime 
{

	public static void main(String[] args) 
	{
		int a[] = {153, 370, 111,22,131,23,443,1234};
		
		for(int i=0; i<a.length; i++)
		{
			int count=0;
			int temp=a[i], sum=0;
			while(temp>0)
			{
				int rem=temp%10;
				temp/=10;
				count++;
			}
			temp=a[i];
//			int sum=0;
			while(temp>0) //153>0  15>0
			{
				int rem=temp%10; // 3 5
				sum = sum + (int)Math.pow(rem, count); //
//				System.out.println("Sum" +sum);
				temp/=10; //15
			}
			if(sum == a[i])
				System.out.println(a[i]);
			
		}
		
			

	}

}
