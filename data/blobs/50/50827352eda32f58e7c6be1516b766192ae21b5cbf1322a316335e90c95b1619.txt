package hm_1_1.monthPack;

public class monthMethod {
    int amount;

    void getMonth(int month) {
        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            amount = 31;
            System.out.println("В этом месяце " + amount + " дней");
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            amount = 30;
            System.out.println("В этом месяце " + amount + " дней");
        } else if (month == 2) {
            amount = 28;
            System.out.println("В этом месяце " + amount + " дней");
        } else {
            System.out.println("Ошибка: Некорректный номер месяца. Введите число от 1 до 12.");
            amount = -1;
        }

    }
}
