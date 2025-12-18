package class14.Homework;
/*2) Create a String that should be combination of letters, numbers and special characters.
Find out how many Alphanumeric(abd AZ 284) characters are there in the String.
* */
public class Task2 {
    public static void main(String[] args) {
        String str = "ghTGD1359878=+))(*&%$@#";
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (Character.isAlphabetic(str.charAt(i))) ;
            if (Character.isDigit(str.charAt(i))) ;
            {
                count++;
            }
        }

                System.out.println(count);

            }

        }




