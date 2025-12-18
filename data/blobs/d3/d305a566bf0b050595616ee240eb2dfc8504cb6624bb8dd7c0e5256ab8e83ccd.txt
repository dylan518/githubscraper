package Lesson4.HomeWork;

public class HWTask2 {
    // Напишите функцию, которая возвращает сумму всех чисел от 1 до 100,
    // но останавливается, если находит число, кратное 42.
    public static void main(String[] args) {
        int result = 0;

        for(int i = 1; i < 100; i++) {
            System.out.println("i = " + i);
            System.out.println("Result = " + result);
            result = result + i;
            if(result % 42 == 0) {
                break;
            }
        }
        System.out.println(result);
    }
}
