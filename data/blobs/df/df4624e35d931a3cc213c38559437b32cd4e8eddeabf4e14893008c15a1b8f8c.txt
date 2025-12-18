/*Реализовать простой калькулятор
Введите первое число: 12
Введите операцию: +
Введите второе число: 1
Ответ: 13 */

import java.util.Scanner;

public class App { // Приглашение о вводу и т.д.
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        System.out.print("Введите число 1: ");
        double num1 = in.nextInt();
        System.out.print("Введите операцию (+,-,*,/): ");
        char oper=in.next().charAt(0);
        System.out.print("Введите число 2: ");
        double num2 = in.nextInt();
        if (oper == '/' && num2 == 0) {
            System.out.printf("Делить на 0 НЕЛЬЗЯ!");
            System.exit(1);
        }
        double result;
        // реализация алгоритма расчеа в ависимости от введенного знака операции
        switch (oper) {
            case '+':
                result = num1 + num2;
                System.out.printf("Результат введенной операции равен %.1f %n \n", result);
                break;
            case '-':
                result = num1 - num2;
                System.out.printf("Результат введенной операции равен %.1f %n \n", result);
                break;
            case '*':
                result = num1 * num2;
                System.out.printf("Результат введенной операции равен %.1f %n \n", result);
                break;
            case '/':
                result = num1 / num2;
                System.out.printf("Результат введенной операции равен %.2f %n \n", result);
                break;
            default:
                System.out.printf("Такой операции нет в калькуляторе, перезапустите программу и введите всё заново");
                break;
        }
        in.close();
        
    }
}
