package lessons.v8.ocp.chapter7;

import java.util.Arrays;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.RecursiveAction;

public class ForkJoinPoolExample {

    public static void main(String[] args) {
        Double[] randomDoubleArray = new Double[712];
        ForkJoinTask<?> task = new MyAction(0, randomDoubleArray.length,
                randomDoubleArray);
        ForkJoinPool pool = new ForkJoinPool();
        pool.invoke(task);
        // Print results
        System.out.println();
        System.out.print("Random doubles: ");
        Arrays.asList(randomDoubleArray).stream()
                .forEach(d -> System.out.print(d + " "));
    }

    static class MyAction extends RecursiveAction {

        private static final long serialVersionUID = 1L;
        private static final int LIMIT = 3;
        private int start;
        private int end;
        Double[] randomDoubleArray;

        public MyAction(int start, int end, Double[] randomDoubleArray) {
            this.start = start;
            this.end = end;
            this.randomDoubleArray = randomDoubleArray;
        }

        @Override
        protected void compute() {

            if (end - start <= LIMIT) {
                for (int i = start; i < end; i++) {
                    randomDoubleArray[i] = (Math.random() * 100);

                }

            } else {
                int middle = start + ((end - start) / 2);
                System.out.println("[start=" + start + ",middle=" + middle
                        + ",end=" + end + "]");
                invokeAll(new MyAction(start, middle, randomDoubleArray),
                        new MyAction(middle, end, randomDoubleArray));
            }

        }
    }

}
