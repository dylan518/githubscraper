package Popup;

import java.util.ArrayList;
import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Windowpopup3 {

	
	public static void main(String[] args) throws InterruptedException 
	{		System.setProperty("webdriver.chrome.driver", "C:\\chromedriver1.exe");
		 ChromeOptions CO=new ChromeOptions();	
		 CO.addArguments("--remote-allow-Origins=*", "ignore-certificate-errors");
		
		 WebDriver  driver=new ChromeDriver(CO); 
          
		 driver.get("https://nxtgenaiacademy.com/multiplewindows/");
		 Thread.sleep(2000);
		 
		 driver.manage().window().maximize();
		 Thread.sleep(2000);
		 
		 driver.findElement(By.xpath("(//button[@id='button1'])[3]")).click();
		 Thread.sleep(2000);
		 
		 //get ids of window popup and main page
		 Set<String> code=driver.getWindowHandles();
		 System.out.println(code);
		 
		 ArrayList<String> hmm=new ArrayList<String>(code);
		 
		 String no1=hmm.get(0);
		 System.out.println(no1);//main page id
		 
		 String no2=hmm.get(1);
		 System.out.println(no2);//window page id
		 
		 driver.switchTo().window(no2);
		 
		 Thread.sleep(2000);
		 driver.findElement(By.xpath("(//Li[@class='menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-7004'])[2]")).click();
		 Thread.sleep(2000);
		 
		 driver.switchTo().window(no1);
		 Thread.sleep(2000);
		 driver.findElement(By.xpath("(//a[@href='https://nxtgenaiacademy.com/python/'])[2]")).click();
				 
				 
				 
				 
				 
				 
				 
				 
}
}