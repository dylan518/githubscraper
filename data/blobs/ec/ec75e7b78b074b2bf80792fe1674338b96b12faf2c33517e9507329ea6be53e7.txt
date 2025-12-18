package Task2;

import java.time.Period;

import static java.lang.System.out;

public class Cat {
    private String name;
    private int age;
    final private String catSound1 = "Мяу!";
    Position position;

    public Cat(String name, int age) {
        this.name = name;
        this.age = age;
        position = Position.NOTHERE;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public Position getPosition() {
        return position;
    }

    public  void catInfo() {
        out.println(name + " " + position);;
    }
    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setPosition(Position position) {
        this.position = position;
    }

    private void thinkAboutGoodMaster(Master master) {
        out.println(name + " думает, что " + master.getName() + " не так уж и плох");
    }

    private void thinkAboutBadMaster(Master master) {
        out.println(name + " думает, что " + master.getName() + " - подлый кожаный мешок");
    }

    public void beCalled(Master master){
        thinkAboutGoodMaster(master);
        if (position == Position.NOTHERE) {
            position = Position.HERE;
        }
        out.println(catSound1);
    }

    public void askMeal(Master master) {
        if (position == Position.NOTHERE) {
            position = Position.HERE;
        }
        out.println(catSound1);
        out.println(catSound1);
        out.println(catSound1);
        master.feedPet(this);
    }

    public void beDrivedAway(Master master) {
        position = Position.NOTHERE;
        thinkAboutBadMaster(master);
    }

}
