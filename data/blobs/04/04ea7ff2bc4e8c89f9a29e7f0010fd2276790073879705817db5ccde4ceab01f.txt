package com.SelfPractise_Selenium;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Browser_OR_Notification_Popup 
{
	public static void main(String[] args) throws InterruptedException 
	{	
		ChromeOptions co = new ChromeOptions();
		co.addArguments("disable-notifications"); // To disable Browser Based Notifications
		
		// disable-notifications ---> Show Notifications (Allow/Block)
		// disable-geolocation	 ---> Show Locations	 (Allow/Block)
		// disable-media-stream	 ---> Show Audio/Video	 (Mute Audio/Video)
		
		System.setProperty("webdriver.chrome.driver", 
		"C:\\Users\\sgsasek\\Desktop\\jAva\\Supporting Files\\chromedriver_win32_101.0.4951.41\\chromedriver.exe");
		WebDriver driver = new ChromeDriver(co);
		driver.manage().window().maximize();
		//driver.get("https://www.hdfcbank.com/");
		driver.navigate().to("https://www.hdfcbank.com/");
		Thread.sleep(3000);
	}
}
