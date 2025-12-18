//---------------O(n^3)-------------------
class LongSubstring
{
	static void longest(String str)
	{
		int res=0;
		int start=0;
		for(int i=0;i<str.length();i++)
		{
			for(int j=i;j<str.length();j++)
			{	int flag=0;
				boolean table[]=new boolean[26];
				for(int k=i;k<=j;k++)
				{
					if(table[str.charAt(k)-'a']==true)
					{
						flag=1;
						break;
					}
					else{
						table[str.charAt(k)-'a']=true;
					}
				}
				if(flag==0)
				{
					if(res<j-i+1)
					{
						start=i;
						res=j-i+1;
					}
				}
				else
				{
					break;
				}
			}
		}
		for(int i=start;i<=start+res-1;i++)
		{
			System.out.print(str.charAt(i));
		}
		System.out.print(" "+res);
	}
	public static void main(String[] args) {
		// String str="heenasulthan";
		String str="geeksforgeeks";
		longest(str);
	}
}
// ---------another approch is O(n^2)---------------
class N2
{
	static void longest(String str)
	{
		int res=0,start=0;
		for(int i=0;i<str.length();i++)
		{
			boolean table[]=new boolean[256];
			for(int j=i;j<str.length();j++)
			{
				if(table[str.charAt(j)]==true)
				{
					break;
				}
				else{
					table[str.charAt(j)]=true;
					if(res<j-i+1)
					{
						start=i;
						res=j-i+1;
					}
				}
			}
		}
		for(int k=start;k<=start+res-1;k++)
		{
			System.out.print(str.charAt(k));
		}
		System.out.print(" "+res);
	}
	public static void main(String[] args) {
		String str="heenasultjhajnj";
		longest(str);
	}
}