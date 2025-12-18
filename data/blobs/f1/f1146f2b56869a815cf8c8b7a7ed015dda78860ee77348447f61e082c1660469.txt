package MiniProjects;

import java.util.Random;

class Tasks implements Runnable{

    private final String taskName;
    private final Random random = new Random();

    public Tasks(String taskName){
        this.taskName = taskName;
    }

    @Override
    public void run(){
        Thread currentThread = Thread.currentThread();

        int taskPriority = random.nextInt(10) + 1;
        currentThread.setPriority(taskPriority);

        System.out.println(taskName + " (Thread ID: " + currentThread.getId() +
                " ,Priority: " + currentThread.getPriority() +" is starting...");

        try {
            int sleeptime = random.nextInt(3) + 1;
            Thread.sleep(sleeptime * 1000);
        }
        catch (InterruptedException e){
            System.out.println(taskName + " (Thread ID: " + currentThread.getId() + ") was interrupted.");
        }
        System.out.println(taskName + " (Thread ID: " + currentThread.getId() +
                ", Priority: " + currentThread.getPriority() + ") completed execution.");
    }
}
public class TaskSchedulerSimulation {

    public static void main(String[] args) {
        Tasks task1 = new Tasks("Task 1");
        Tasks task2 = new Tasks("Task 2");
        Tasks task3 = new Tasks("Task 3");

        Thread thread1 = new Thread(task1);
        Thread thread2 = new Thread(task2);
        Thread thread3 = new Thread(task3);

        thread1.start();
        thread2.start();
        thread3.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
        }
        catch (InterruptedException e){
            System.out.println("Main thread interrupted.");
        }

        System.out.println("\nAll tasks have completed execution.");
    }
}
