package FinalTasks.Task1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Напишите программу конвертер валют.
 * Программа должна переводить рубли в доллары по текущему курсу. Пользователь вводит текущий курс и количество рублей.
 * Итоговое значение должно быть округлено до двух знаков после запятой.
 * Пример для теста работы программы:
 * - Курс доллара: 67,55
 * - Количество рублей: 1000
 * - Итого: 14,80 долларов
 */

public class Task1 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        double rate;
        double amount;

        System.out.println("Введите текущий курс: ");
        while (true) {
            try {
                rate = Double.parseDouble(reader.readLine());
                break;
            } catch (NumberFormatException e) {
                System.out.println("Вы ввели что-то другое. Попробуйте еще раз ввести число: ");
            }
        }

        System.out.println("Введите количество рублей: ");
        while (true) {
            try {
                amount = Double.parseDouble(reader.readLine());
                break;
            } catch (NumberFormatException e) {
                System.out.println("Вы ввели что-то другое. Попробуйте еще раз ввести число: ");
            }
        }
        System.out.printf("Курс доллара: %.2f\nКоличество рублей: %.2f\nИтого: %.2f долларов", rate, amount, (amount / rate));
    }
}