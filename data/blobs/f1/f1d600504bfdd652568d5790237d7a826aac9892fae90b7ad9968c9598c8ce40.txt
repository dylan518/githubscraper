package animal;

import interfaceAnimal.Climbable;
import interfaceAnimal.Swimable;

public class Bear implements Climbable, Swimable {
    String name;

    public Bear(String name) {
        this.name = name;
    }

    @Override
    public void climb() {
        System.out.println("Теперь я умею карабкаться");

    }

    @Override
    public void swim() {
        System.out.println("Я медьведь и теперь я умею плавать");
    }

    @Override
    public void speak() {
        System.out.println("Теперь я умею говорить");
    }
}
