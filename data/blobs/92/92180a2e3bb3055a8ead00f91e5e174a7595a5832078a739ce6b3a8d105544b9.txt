package LectureTestArea;

import java.io.FileInputStream;
import java.io.IOException;

//Read data stream as input and print to the terminal
public class AreaTest2 {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("LectureTestArea/file1.dat");
        int c;
        while ((c = fis.read()) != -1 ) {
            System.out.println((char) c);
        }
        fis.close();

    }
}
