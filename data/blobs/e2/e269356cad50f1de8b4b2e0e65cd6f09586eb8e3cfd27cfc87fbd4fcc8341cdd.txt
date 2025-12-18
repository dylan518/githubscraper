package com.learning.threads;

public class SynchronisationDemo {

    public static void main(String args[]) {

        MathUtils utils = new MathUtils();

        HelloThread helloThread = new HelloThread(utils);
        Thread helloRunnable = new Thread(new HelloRunnable(utils));

        helloThread.start();
        helloRunnable.start();
    }
}
