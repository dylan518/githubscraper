package pingPong;

public class Test {
    public static void main(String[] args) throws InterruptedException {
        Print print = new Print();
        Game game1 = new Game(print);
        Game game2 = new Game(print);
        game1.start();
        game2.start();
        game1.join();
        game2.join();
        System.out.println(print.i);
    }
}
