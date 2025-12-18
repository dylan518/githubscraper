public class Main {
    public static void main(String[] args) {
        // Создание объектов класса Аптека
        Apteka apteka1 = new Apteka("Морг Моргает");
        apteka1.inizialize(new String[]{"Капли от простуды", "Обезболивающее", "Антибиотик"},
                new double[]{100.0, 150.0, 200.0});

        Apteka apteka2 = new Apteka("Морг Не моргает");
        apteka2.inizialize(new String[]{"Сироп от кашля", "Витамины", "Противовирусное"},
                new double[]{80.0, 120.0, 180.0});

        // Проверка методов
        System.out.println(apteka1.получитьИнформацию());
        System.out.println("Цена самого дорогого лекарства в аптеке 1: " + apteka1.ценаСамогоДорогогоЛекарства());
        System.out.println("Общая стоимость лекарств в аптеке 1: " + apteka1.общаяСтоимость());

        System.out.println(apteka2.получитьИнформацию());
        System.out.println("Цена самого дорогого лекарства в аптеке 2: " + apteka2.ценаСамогоДорогогоЛекарства());
        System.out.println("Общая стоимость лекарств в аптеке 2: " + apteka2.общаяСтоимость());
    }
}