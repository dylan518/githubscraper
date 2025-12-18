package com.concurrencyJJ.executors;

import java.util.List;
import java.util.concurrent.*;

public class ExecutorServiceExample5 {

    public static void main(String[] args) {
        ExecutorService service = Executors.newFixedThreadPool(1);
        List<Callable<String>> callables = List.of(
                newCallable("Task-1", 100),
                newCallable("Task-2", 200),
                newCallable("Task-3", 300)
        );

        try {
            List<Future<String>> futures = service.invokeAll(callables);
            futures.forEach(future -> {
                try {
                    System.out.println(future.get());
                } catch (InterruptedException | ExecutionException e) {
                    e.printStackTrace();
                }
            });
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        service.shutdown();
    }

    private static Callable<String> newCallable(String taskName, long millis) {
        return new Callable<String>() {
            @Override
            public String call() throws Exception {
                try {
                    Thread.sleep(millis);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                return Thread.currentThread().getName() + ": " + taskName;
            }
        };
    }
}
