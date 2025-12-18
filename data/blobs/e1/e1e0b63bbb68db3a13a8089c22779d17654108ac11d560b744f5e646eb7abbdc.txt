package ru.alex_life.generics.game;

/**
 * Видео-курс Черный пояс.
 * 3. Generics
 * 3.4. Пример на generics
 *
 * Создаем игру "Что где когда" в которой будут:
 * Участники общей толпой - Participant
 * В каждой команде будут два человека (но можно сколько угодно)
 * И есть три лиги - Школьная лига, Студенческая и Рабочая лига
 *
 * @author Alex_life
 * @version 1.0
 * @since 05.10.2021
 */
public abstract class Participant {
    private String name;
    private int age;

    public Participant(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
