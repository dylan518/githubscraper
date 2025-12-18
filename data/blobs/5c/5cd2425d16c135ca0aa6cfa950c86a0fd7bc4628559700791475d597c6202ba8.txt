import java.util.ArrayList;
import java.util.List;

public class Game {
    List<Bird> birds = new ArrayList<Bird>();

    Game(List<Bird> birds) {
        this.birds = birds;
    }

    public void play() {
        System.out.println("Game Starts :");
        for (Bird bird : birds) {
            bird.fly();
            bird.makeSound();
            bird.attack();
            System.out.println("-------------------");
        }
    }
}
