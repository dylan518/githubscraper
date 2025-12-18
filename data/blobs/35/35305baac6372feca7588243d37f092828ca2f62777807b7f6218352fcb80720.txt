package com.yqq.thread.ch02.p115;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        MyService service = new MyService();
        ThreadA a = new ThreadA(service);
        a.setName("A");
        a.start();
        Thread.sleep(50);
        ThreadB b = new ThreadB(service);
        b.setName("B");
        b.start();


    }
}
