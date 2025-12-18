package basic;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

import utill.DriverConnection;

public class CrossBrowser {
	
	@Parameters({"username","password","browser"})
	@Test
	public void login(String uname, String pass,String browser)
	{
		WebDriver driver=null;
		if(browser.equals("chrome"))
		{
			System.setProperty("webdriver.chrome.driver", "C:\\Chintan_work\\seleniumdata\\chromedriver.exe");
			driver = new ChromeDriver();
		}
		else if(browser.equals("ff"))
		{		
			System.setProperty("webdriver.gecko.driver", "C:\\Chintan_work\\seleniumdata\\geckodriver.exe");
			 driver = new FirefoxDriver();
		}
		
		driver.get("https://www.fb.com");
		driver.findElement(By.id("email")).sendKeys(uname);
		driver.findElement(By.id("pass")).sendKeys(pass);
		driver.findElement(By.name("login")).click();
	}
}
