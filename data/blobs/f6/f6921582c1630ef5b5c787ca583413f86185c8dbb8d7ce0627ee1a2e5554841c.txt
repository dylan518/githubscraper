package LoginTestCases;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

public class TestCase1 {
	
	//Using Parameter method
	
	@Test
	@Parameters({"username","password"})
	public void test1(String username,String pass) {
	System.setProperty("webdriver.chrome.driver", "C:\\Users\\ARO EDWIN\\Downloads\\chromedriver\\chromedriver.exe");
	ChromeDriver driver=new ChromeDriver();
	driver.get("https://opensource-demo.orangehrmlive.com/");
	
	WebElement user=driver.findElement(By.id("txtUsername"));
	user.sendKeys(username);
	
	WebElement password=driver.findElement(By.id("txtPassword"));
	password.sendKeys(pass);
	
	WebElement clickbtn=driver.findElement(By.id("btnLogin"));
	clickbtn.click();
	driver.quit();
	
	}

}
