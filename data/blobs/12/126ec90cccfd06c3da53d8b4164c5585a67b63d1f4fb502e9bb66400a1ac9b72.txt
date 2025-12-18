package day02;

/*
    赋值运算符：
        =, +=, -=, *=, /=, %=  包含强制转换
*/

public class FuZhiDemo1 {
    public static void main(String[] args) {
        int a = 10;     // 正确读法：将数值常量10赋值给int类型的变量a

//        a += 1;
//        a -=1;
//        a *= 2;
//        a /= 3;
        a %= 4;
        System.out.println(a);

        byte b=10;
        b+=2;   // 包含强制转换  等价于 b = (byte)(b+2)
//        b=b+3;  // 不包含强制转换
        System.out.println(b);

    }
}
