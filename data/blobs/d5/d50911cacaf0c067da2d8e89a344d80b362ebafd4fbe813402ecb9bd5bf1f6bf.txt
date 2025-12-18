package synchronisation.SemaphoreDemo;
import java.util.*;
import java.util.concurrent.Semaphore;

public class Producer implements Runnable{

    private Queue<Shirt> store;

    private String name;

    private int MaxSize;

    Semaphore semaphoreproducer;
    Semaphore semaphoreconsumer;

    public Producer(Queue<Shirt> store,String name,int MaxSize,Semaphore semaphoreproducer,Semaphore semaphoreconsumer){
        this.store = store;
        this.name = name;
        this.MaxSize = MaxSize;
        this.semaphoreproducer = semaphoreproducer;
        this.semaphoreconsumer = semaphoreconsumer;
    }


    public void run(){
        while(true) {
                try{
                    semaphoreproducer.acquire();
                    System.out.println("inside producer Current size :" + store.size());
                    store.add(new Shirt());
                    semaphoreconsumer.release();
                }
                catch(Exception e){
                    e.getMessage();
                }

            }
        }

    }
