package lab16;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.lang.ArrayIndexOutOfBoundsException;

public class task5 {
    public static void main(String[] args) {

        File file = new File("resourser/task8139/test1.txt");
        int x = 0;
        int count = 0;

        try {
            Scanner s = new Scanner(file);

            while (s.hasNext()) {
                String line = s.nextLine();
                x = Integer.parseInt(line);
                task8139(line);
                boolean result = task8139(line);

                if (result) {
                    count++;

                }

            }

            System.out.println(count);

        } catch (FileNotFoundException ex) {
            System.out.print("Файл не найден " + file.getAbsolutePath());
        } catch (java.lang.ArrayIndexOutOfBoundsException r) {
            System.out.print("Не удается считать число");
        } catch (IllegalArgumentException u) {
            System.out.print("Некорректное число");
        }
    }

    public static boolean task8139(String x) {

        char[] num = x.toCharArray();
        if (num.length != 4) {
            throw new IllegalArgumentException("Некорректное число");
        }


        if (num[0] == num[1]) {
            return true;
        } else if (num[1] == num[2]) {
            return true;
        } else return num[2] == num[3];

    }

}


