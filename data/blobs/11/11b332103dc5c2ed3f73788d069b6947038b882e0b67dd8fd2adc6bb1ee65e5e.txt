package recursion;

public class ReformatPhoneNumber1694 {
    public static String getFormat(String s) {
        int n = s.length(); // 123-45-67
        String result = " ";
        if (n == 2) { // điều kiện dừng
            return s;
        } else if (n == 4) { // điều kiện dừng
            return s.substring(0, 2) + '-' + s.substring(2, n);
        } else if (n >= 3) {
            if (n == 3) { // có thể thêm điều kiện dừng là 3 nữa ở trên thì ko phải viết đoạn này.
                result = s.substring(0, 3);
            } else { // với vd là 1234567 thì vì n = 7 nên đầu tiên code sẽ chạy vào đây.
                result = s.substring(0, 3) + '-' + getFormat(s.substring(3, n));
            }
        }
        return result;
    }

    public static String reformatNumber(String number) {
        String newStr = "";
        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) != ' ' && number.charAt(i) != '-') {
                newStr = newStr + number.charAt(i);
            }
        }
        // bước trên để loại bỏ " " và - có thể dùng replaceAll:
        // number = number.replaceAll("[ -]", "");
        System.out.println(newStr);
        return getFormat(newStr);
    }

    public static void main(String[] args) {
        // String number = "1-23-45 6";
        String number = "123 4-567";
        System.out.println(reformatNumber(number));
    }
}
