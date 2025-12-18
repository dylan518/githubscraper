package assignments.multithreading;

/**
 * 1. Write a Java program that starts two threads and each thread will print the numbers
 * from 1 - 4. While performing this task each thread will be at sleep for two seconds
 * Sample output:
 *
 * 1
 * 1
 * 2
 * 2
 * 3
 * 3
 * 4
 * 4
 */

public class Question1 extends Thread {
    public void run() {
        for (int i = 1; i <= 4; i++) {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(i);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Question1 t1 = new Question1();
        Question1 t2 = new Question1();
        t1.start();
        t2.start();
    }
}
