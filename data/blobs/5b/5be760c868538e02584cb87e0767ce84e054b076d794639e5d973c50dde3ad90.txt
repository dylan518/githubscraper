import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;

public class MoreThanSix {
    public static void main(String[] args) throws Exception {
        String fileName1 = "C:\\Users\\UMAG\\Desktop\\asc.txt";
        String fileName2 = "C:\\Users\\UMAG\\Desktop\\asc2.txt";

        BufferedReader reader = new BufferedReader(new FileReader(fileName1));
        ArrayList<String> list = new ArrayList<>();
        while (reader.ready()) {
            String[] str = reader.readLine().split(" ");
            for (String s : str) {
                list.add(s);
            }

        }

        FileWriter writer = new FileWriter(fileName2);
        String ans = "";
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).length() > 6 && i == (list.size() - 1)) {
                ans = ans + list.get(i);
                break;

            }
            if (list.get(i).length() > 6) {
                ans = ans + list.get(i) + ",";

            }


        }
        writer.write(ans);
        reader.close();
        writer.close();
    }
}
