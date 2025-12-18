package STRINGS;

public class P4 {

public static void main(String[] args) {
	String s="hi@123";
	char[]ch=s.toCharArray();
	int count=0;
	for(int i=0;i<ch.length;i++)
	{
		if(ch[i]>='0'&& ch[i]<='9')
		{
			count++;
		}
	}
System.out.println("count of digits:"+count);
}
}

