import java.util.Scanner;
class SimpleRepeat
{
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the values:");
        String a = scan.nextLine();
        String result = "";
        String temp = "";
        for(int i = 0;i<a.length();i++)
        {
            char b = a.charAt(i);
            if ((b>='A' && b<='Z')|| (b>='a'&& b<='z'))
            {
                temp += b;
            }
            else if(b>='0' && b<='9')
            {
                int t= b -'0';
                for(int j = 0; j<t;j++)
                {
                    result += temp; 
                }
                temp = "";
            }
        }
        result +=temp;
        System.out.print(result);
    }
}