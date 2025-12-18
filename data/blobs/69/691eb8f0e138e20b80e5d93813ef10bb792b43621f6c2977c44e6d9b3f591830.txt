package ru.example;
//В качестве задачи предлагаю вам реализовать код для демонстрации парадокса Монти Холла (Парадокс Монти Холла — Википедия )
// и наглядно убедиться в верности парадокса
//        (запустить игру в цикле на 1000 и вывести итоговый счет).
//        Необходимо:
//        Создать свой Java Maven или Gradle проект;
//        Подключить зависимость lombok.
//        Можно подумать о подключении какой-нибудь математической библиотеки для работы со статистикой
//        Самостоятельно реализовать прикладную задачу;
//        Сохранить результат в HashMap<шаг теста, результат>
//        Вывести на экран статистику по победам и поражениям
//
//        Работы принимаются в виде ссылки на гит репозиторий со всеми ключевыми файлами проекта
//Есть три закрытые двери: за одной из них спрятан главный приз (например, автомобиль), а за двумя другими — "утешительные призы" (обычно козы).
//        Выбор игрока:
//
//        Игрок выбирает одну из дверей. Он не знает, где находится главный приз.
//        Действия ведущего:
//
//        Ведущий, который знает, за какой дверью находится приз, открывает одну из оставшихся дверей, за которой точно находится коза.
//        Выбор игрока (второй раунд):
//
//        У игрока есть выбор:
//        Остаться при своём первоначальном выборе.
//        Переключиться на другую закрытую дверь.
//        Результат:
//
//        После того как игрок делает свой окончательный выбор, ведущий открывает выбранную дверь, и становится ясно, выиграл ли игрок главный приз.


import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Количество симуляций
        int simulations = 10000;

        // Подсчет побед
        int winsWhenSwitching = 0;
        int winsWhenStaying = 0;

        Random random = new Random();

        for (int i = 0; i < simulations; i++) {
//     Шаг 1:        Распределение призов за дверями
            HashMap<Integer, String> map = new HashMap<>();//Создаем список призов,что будет храниться за дверьми
            map.put(1, "Коза");
            map.put(2, "Коза");
            map.put(3, "Коза");

            // Случайно выбираем дверь с призом
            int prizeDoor = random.nextInt(3) + 1;
            map.put(prizeDoor, "Авто");

            //  Шаг 2: Участник случайно выбирает дверь
            int participantChoice = random.nextInt(3) + 1;

            // Шаг 3: Ведущий открывает одну из оставшихся дверей с козой
            List<Integer> remainingDoors = new ArrayList<>();
            for (int door : map.keySet()) {
                if (door != participantChoice && !map.get(door).equals("Авто")) {// если это не выбор участника и элемент не авто
                    remainingDoors.add(door);// добавляем в список дверь с козой, которую открыл ведущий
                }
            }
            // Если оставшихся дверей нет, пропускаем эту итерацию
            if (remainingDoors.isEmpty()) {
                continue;
            }
            int hostOpens = remainingDoors.get(random.nextInt(remainingDoors.size()));

            // Шаг 4: Определяем, какая дверь остаётся
            int remainingDoor = 0;
            for (int door : map.keySet()) {
                if (door != participantChoice && door != hostOpens) {
                    remainingDoor = door;
                    break;
                }
            }

            // Шаг 5: Симулируем оба сценария
            // Участник остаётся при своём выборе
            if (participantChoice == prizeDoor) {
                winsWhenStaying++;
            }

            // Участник меняет выбор
            if (remainingDoor == prizeDoor) {
                winsWhenSwitching++;
            }
        }

        // Результаты
        System.out.println("Побед при смене выбора: " + winsWhenSwitching);
        System.out.println("Побед при сохранении выбора: " + winsWhenStaying);

        // Вероятности
        double switchWinRate = (double) winsWhenSwitching / simulations * 100;
        double stayWinRate = (double) winsWhenStaying / simulations * 100;

        System.out.println("Вероятность выигрыша при смене: " + switchWinRate + "%");
        System.out.println("Вероятность выигрыша при сохранении: " + stayWinRate + "%");
    }
}
