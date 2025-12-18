/*
 * Copyright (c) 2024. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 * Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
 * Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
 * Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
 * Vestibulum commodo. Ut rhoncus gravida arcu.
 */
package com.rp.sec02;

import com.rp.sec02.assignment.StockPublisher;
import org.reactivestreams.Subscriber;
import org.reactivestreams.Subscription;

import java.util.concurrent.CountDownLatch;

public class Lec10AssignmentStockObserver {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch countDownLatch = new CountDownLatch(1);
        StockPublisher.getPrice()
                .subscribeWith(new Subscriber<Integer>() {

                    Subscription s;

                    @Override
                    public void onSubscribe(Subscription s) {
                        this.s = s;
                        s.request(Integer.MAX_VALUE);
                    }

                    @Override
                    public void onNext(Integer price) {
                        System.out.println(price);
                        if (price > 105 || price < 95) {
                            s.cancel();
                            countDownLatch.countDown();
                        }
                    }

                    @Override
                    public void onError(Throwable t) {
                        countDownLatch.countDown();
                    }

                    @Override
                    public void onComplete() {
                        System.out.println("complete");
                        countDownLatch.countDown();
                    }
                });
        countDownLatch.await();
    }
}