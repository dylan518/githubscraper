package com.xiangyanlin.redis.redisoperationdemo.juc.model;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * @author XiangYanLin
 * @date 2021/1/17
 */
public class ShareResource {
    private int number=1;
    public Lock lock = new ReentrantLock();
    public Condition c1 = lock.newCondition();
    public Condition c2 = lock.newCondition();
    public Condition c3 = lock.newCondition();

    public void print(Condition await,Condition signal,int n,int target,int cond){
        lock.lock();
        try {
            while (number!=cond){
                await.await();
            }
            for (int i = 1; i <=n ; i++) {
                System.out.println(Thread.currentThread().getName()+"\t"+i);
            }
            number = target;
            //通知第2个
            signal.signal();
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            lock.unlock();
        }
    }
}
