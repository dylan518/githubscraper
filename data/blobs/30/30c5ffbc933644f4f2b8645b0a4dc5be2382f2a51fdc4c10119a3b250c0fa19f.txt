package Test_Demo;

import java.util.regex.Pattern;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Test2 {

	public static void main(String[] args) {
		
		// Browser Open
		WebDriverManager.chromedriver().setup();
		ChromeDriver driver=new ChromeDriver();
		driver.get("https://demo.guru99.com/test/newtours/register.php");
		driver.manage().window().maximize();
		
		// Element -- Actions 
		
		
		custom_SendKeys(driver,"Test");
		
		WebElement txt_LastName=driver.findElement(By.xpath("//input[@name='lastName']"));
		
		
		
	}

	public static void custom_SendKeys(WebDriver driver,String value) {
		WebElement element=driver.findElement(By.xpath("//input[@name='firstName']"));
		try {
			if(element.isEnabled() && element.isDisplayed()) {
				element.sendKeys(value);
			}else {
				System.out.println("message");
			}
		   
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}
		
   public static void custom_click(WebElement element) {
	   try {
		   element.click();
	   }catch(Exception e) {
		   System.out.println(e.getMessage());
	   } 
   }
	
	
}
