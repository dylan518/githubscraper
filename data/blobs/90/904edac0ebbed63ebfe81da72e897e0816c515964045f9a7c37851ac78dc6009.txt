package Threads;

public class HelloWithThread extends Thread {
	private String name = null;
	public HelloWithThread(String threadName)
	{
		name = threadName;
	}
	public void run()
	{
		for(int i=0; i<10; i++)
		{
			System.out.println(i+" Hello Thread "+name);
		    try
		    {
		    	Thread.sleep(1000);
		    	System.out.println(" it should sleep for 1sec.");
		    }
		    catch(Exception x)
		    {
		    	x.printStackTrace();
		    }
		}
	}
	public static void main(String[] args) {
		HelloWithThread t1=new HelloWithThread("Yuvraj");
		HelloWithThread t2=new HelloWithThread("Virat");
		t1.start();
		t2.start();
		
		for(int i=0; i<10; i++)
		{
			System.out.println(" Threads are rRunning...");
		}
		
	}

}
