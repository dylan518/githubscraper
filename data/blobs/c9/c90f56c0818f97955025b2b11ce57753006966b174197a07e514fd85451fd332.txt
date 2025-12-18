package Assertion;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotEquals;
import static org.testng.Assert.assertNull;
import static org.testng.Assert.assertTrue;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class AssertFalse {
	public void main() {
		String value="null";
	
	String expected_url="https://demowebshop.tricentis.com/";
	WebDriver driver=new ChromeDriver();
	driver.manage().window().maximize();
	driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(15));
	driver.get("https://www.demowebshop.tricentis.com/");
	String actual_url=driver.getCurrentUrl();
	assertEquals(expected_url,actual_url,"iam not in dws");
	System.out.println("i am in dws");
	driver.findElement(By.className("ico-register")).click();

	assertNotEquals(expected_url,actual_url,"iam not in reg pg");
	System.out.println("i am in reg pg");
	WebElement reg_title=driver.findElement(By.xpath("//div[@class='page-title']/"));
	assertTrue(reg_title.isDisplayed(),"register title is not displayed");
	System.out.println(" reg title is displayed");
	
	assertNull(value,"Value container is not Null");
	System.out.println("val container is null");
	

}
}