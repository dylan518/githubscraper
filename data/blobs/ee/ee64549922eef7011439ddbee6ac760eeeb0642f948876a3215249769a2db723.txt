package _19_io_bonus.doc_ghi_file_text;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class TypeText {
    public static void main(String[] args) throws IOException {
        writeFileText("src\\_19_io_bonus\\filetext.txt");

        readFileText("src\\_19_io_bonus\\filetext.txt");
    }

    public static void writeFileText(String path) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(path));
        bw.write("Hello world!!!" + "\nI am Hero");
        bw.close();
    }

    public static void readFileText(String path) throws IOException {
        List<String> strings = new ArrayList<>();
        BufferedReader br = new BufferedReader(new FileReader(path));

        String line;
        while ((line = br.readLine()) != null) {
            strings.add(line);
        }
        br.close();
        for (String s : strings) {
            System.out.println(s);
        }
    }
}
