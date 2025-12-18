package ua.com.kisit_course.groupe372.unit10.example5;

public class Main {

    public static void main(String[] args) {

        Res res =new Res();

        for (int i = 0; i < 10; i++) {

            Thread thread = new Thread(new MyThread(res));
            thread.setName("Thread " + i);
            thread.start();

        }

    }


}
