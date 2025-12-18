package com.pack;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Example2 
{

	public static void main(String[] args) throws Exception 
	{
		WebDriver driver;
		WebDriverManager.chromedriver().setup();
		driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("https://datatables.net/examples/advanced_init/dt_events.html");
		
		int pagesize = driver.findElements(By.cssSelector("nav[aria-label='pagination']>button")).size();
		System.out.println("Pagesize : " + pagesize);
		
		for(int i=3;i<pagesize-1;i++)
		{
			String pagalocator = "nav[aria-label='pagination']>button:nth-child("+i+")";
			driver.findElement(By.cssSelector(pagalocator)).click();
			
			List<WebElement> names = driver.findElements(By.cssSelector("table#example>tbody>tr>td:nth-child(1)"));
			for(WebElement name:names)
			{
				System.out.println(name.getText());
			}
			
			System.out.println(" ------- End of Page ------- " + (i-2));
			Thread.sleep(3000);
			
		}
	}

}
