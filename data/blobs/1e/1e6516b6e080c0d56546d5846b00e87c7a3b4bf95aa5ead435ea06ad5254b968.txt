package ac7week3.ac0726.file_1;


/*
        버퍼 없이 진행시
        1. 크기를 똑같이 맞추기 힘들다
        2. 속도가 느리다.


 */

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Ex07 {
    public static void main(String[] args) throws IOException {
        FileInputStream fileInputStream = new FileInputStream("idealC-2023.1.3.exe");
        FileOutputStream fileOutputStream = new FileOutputStream("copy.2023.exe");

        byte[] bufferIn = new byte[1000000000];
        byte[] bufferOut = new byte[1000000000];


        fileInputStream.read(bufferIn);
        fileOutputStream.write(bufferOut);

        System.out.println("복사 완료");
        fileInputStream.close();
        fileOutputStream.close();
    }
}
