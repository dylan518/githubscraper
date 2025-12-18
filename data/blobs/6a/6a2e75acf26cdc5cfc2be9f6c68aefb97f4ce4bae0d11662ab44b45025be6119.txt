package org.telatenko;

/*
Написать код, в ходе выполнения которого будет генерироваться OutOfMemoryError.
Сделать 3 разных варианта получения этой ошибки.
Код запускать с указанием параметров памяти JVM (xms, xmx и так далее)
*/
public class OutOfMemoryErrorClass {

    public static class OutOfMemoryErrorExample1 {
        public static void main(String[] args) {
            throw new OutOfMemoryError();
        }
    }

    public static class OutOfMemoryErrorExample2 {
        public static void main(String[] args) {
            String x = "1";
            while (true) {
                x = (x + x);
            }
        }
    }

    public static class OutOfMemoryErrorExample3 {
        public static void main(String[] args) {
            String[] strings = new String[1000000];
            for (int i = 0; i < strings.length; i++) {
                strings[i] = new String(new char[1000000]).intern();
            }
        }
    }

    public static class OutOfMemoryErrorExample4{
        public static void main(String[] args) {
            try {

            } finally {
              throw new OutOfMemoryError();
            }
        }
    }

}
