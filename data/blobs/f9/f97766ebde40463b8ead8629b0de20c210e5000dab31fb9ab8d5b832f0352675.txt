package arrayAttempt2;

public class EqualityOfTwoArrAss14 {

	public static void main(String[] args) {
		int[] a = {1,2,3,4,5,6,7,8,9};
		int[] b = {1,2,3,4,5,6,7,8};
		boolean flag = true;
		if(a.length!=b.length)
		{
			System.out.println("Not Same from if");
		}
		else
		{
			for (int i = 0; i < b.length; i++) {
				if(a[i]!=b[i])
				{
					flag=false;
				}
			}
			if(flag)
				System.out.println("Two Arrays Are Same");
			else
				System.out.println("Not Same");
		}
				

	}

}
