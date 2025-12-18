public class ThreadExample5 {
    public static void main(String[] args) {
        SumThread sumThread = new SumThread();
        sumThread.setTo(10); // to에 10 할당
        sumThread.start(); // 실행 대기

        try {sumThread.join();} catch (Exception e) {}

        System.out.println(String.format("1부터 %d까지의 합 : %d", sumThread.getTo(), sumThread.getSum()));
    }
}

class SumThread extends Thread {
    private long sum;
    private  int to;

    public long getSum() {
        return sum;
    }
    public int getTo() {
        return to;
    }
    public void setTo(int to) {
        this.to = to;
    }
    @Override
    public void run() {
        for (int i = 1; i <= to; i++) {
            sum += i;
        }
    }
}