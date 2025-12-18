package Utils;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
/**
 *
 * @author boonie-pt
 */
public class MyValidation {
    
    public static boolean checkString(String s, String pattern)
    {
        return s.matches(pattern);
    }
    
    public static boolean isEmptyString(String s)
    {
        return s.trim().isEmpty();
    }
    
    public static boolean isName(String name)
    {
        return checkString(name, "[a-zA-Z]{2,35}|null");
    }
    
    public static boolean isPhone(String phone)
    {
        return checkString(phone, "^0(([0-9]){9})");
    }

    public static boolean isNumeric(String str) {
        try {
            Integer.valueOf(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static LocalDate checkDate(String dateString) throws Exception {
        DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return LocalDate.parse(dateString.trim(), dateFormatter);
    }
    
    public static boolean isValidDate(String date, String format) {
        SimpleDateFormat dateFormat = new SimpleDateFormat(format);
        dateFormat.setLenient(false);
        try {
            dateFormat.parse(date.trim());
        } catch (ParseException pe) {
            return false;
        }
        return true;
    }
    
    public static void getEnter(String message) {
        Scanner sc = new Scanner(System.in);
        System.out.print(message);
        do {
            if (sc.nextLine().isEmpty() || sc.next().equals(""))
                return;
        } while (true);
    }
}

