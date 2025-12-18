package com.xsq.io.ConvertedStream;

import java.io.*;

public class testConvertedStream02 {
    public static void main(String[] args) throws IOException {
        /*
         * 1.创建OutputStreamWriter对象，构造方法中传递字节输出流和指定的編码表名称。
         * 2.使用OutputStreamWriter对象中的方法write，把字符转换为字节存储到缓冲区中（编码）。
         * 3.使用OutputStreamWriter对象中的方法flush，把内存缓冲区中的字节刷新到文件中（使用字节流写字节的过程）。
         * 4.释放资源。
         * */
        //OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("myCharStream\\osw.txt"));
        OutputStreamWriter osw = new OutputStreamWriter(new
                FileOutputStream("JavaBase\\src\\com\\xsq\\io\\a.txt", true), "GBK");
        osw.write("中国");
        osw.flush();
        osw.close();

        /*
         * 1.创建InputStreamReader对象，构造方法中传递字节输入流和指定的编码表名称。
         * 2.使用InputStreamReader对象中的方法read，读取文件。
         * 3.释放资源。
         * */
        //InputStreamReader isr = new InputStreamReader(new FileInputStream("myCharStream\\osw.txt"));
        InputStreamReader isr = new InputStreamReader(new
                FileInputStream("JavaBase\\src\\com\\xsq\\io\\a.txt"), "GBK");
        //一次读取一个字符数据
        int ch;
        while ((ch = isr.read()) != -1) {
            System.out.print((char) ch);
        }
        isr.close();
    }
}
