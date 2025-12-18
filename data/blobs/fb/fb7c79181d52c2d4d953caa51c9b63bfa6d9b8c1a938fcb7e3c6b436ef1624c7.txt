public class ThreadingByImplementing implements Runnable {

    public void run() {
        System.out.println("Inside run method");
    }

    public static void main(String[] args) {
        ThreadingByImplementing obj = new ThreadingByImplementing();
        Thread thread = new Thread(obj);
        thread.start();

        for(int i=1;i<=5;i++)
            System.out.println(i);
        //System.out.println("Main method");
    }
}
