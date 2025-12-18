package Concurrancies;

public class SleepInterruptedExample {
    public static void main(String[] args) {
        Thread sleeperThread = new Thread(() -> {
            try {
                System.out.println("About to wait 10 seconds...");
                Thread.sleep(10000);
                System.out.println("Wake up after 10 seconds...");
            } catch (InterruptedException e) {
                System.out.println("Thread was interrupted during sleep!");
            }
        });

        sleeperThread.start();

        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        sleeperThread.interrupt();

        /*
        About to wait 10 seconds...
        Thread was interrupted during sleep!
         */
    }
}
