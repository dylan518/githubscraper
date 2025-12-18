package Codewars;

import schildt.chapter5.array.StringArrays;

public class kata34 {
    public static void main(String[] args) {
        System.out.println(getCount("Java"));
        System.out.println(getCount("Harder"));
        System.out.println(getCount("Than"));
        System.out.println(getCount("JavaScript"));

    }
        // написать метод который будет возвращать (количество) гласных букв в заданной строке.
        // Рассматриваемые буквы a, e, i, o, u .
        // входная строка будет состоять только из строчных букв или пробелов.

        // У нас имеется англ. алфавит, нас интересуют гласные буквы a, e, i, o, u.
        // Написать метод, который будет принимать строку String Str, и возвращать число гласных букв.


    
    public static int getCount(String str) {
        int vowelsCount = 0;

        char[] wowelsArray = str.toCharArray();       // возвращаемое значение char[]
        for (int i = 0; i < wowelsArray.length; i++) {     // Бежим по массиву букв

            if (wowelsArray[i] == 'a' || wowelsArray[i] == 'e' || wowelsArray[i] == 'i' || wowelsArray[i] == 'o' || wowelsArray[i] == 'u') {
                vowelsCount++;    // повторяем поиск, если нашли гласную букву a, e, i, o, u .
            }
        }
        return vowelsCount;         // возвращаем гласные буквы из строки
    }
}
       // String [] strArrays = { "a", "e", "i", "o", "u" };
        //String s = "a";
        //for (int i = 0; i < strArrays.length; i++) {
          //  if (s.equals(strArrays[i])) {



            



      //  int count = 0;
       // for (int i = 0; i < .length(); i++) {
          //  if (str.charAt(i) == 0 || str.charAt(i) == 4 || str.charAt(i) == 8 || str.charAt(i) == 14 || str.charAt(i) == 21)
          //  if (str.charAt(i) == "a" || str.charAt(i) == "e" || str.charAt(i) == "i" || str.charAt(i) == "o" || str.charAt(i) == "u")


      //  count++;
       // }
    //    return vowelsCount;
  //  }
//}
