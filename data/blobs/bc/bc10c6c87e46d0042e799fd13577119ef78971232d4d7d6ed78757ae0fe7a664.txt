package testngSessions;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class AmazonTestWithBM_class1 {
	
	// In the below code - three times the browser will be called and three times the browser will be closed
	
	// this approach is recommended as browser may get hang in between if we use BeforeTest and the rest test cases may not execute
	// Hence BeforeMethod is best to be used and it will call the browser before every test method.
	
	// We can use Priority as below -which will help us to execute the test method in the same order 
	// We can also give - negative number as well in the priority.
	
	// *We need to follow AAA Rule:
	// AAA stands for: Arrange, Act, Assert 
	// 1 test case-should have 1 assert only
	
	
	 WebDriver driver;

		@BeforeMethod
		public void setup() {

			driver = new ChromeDriver();
			driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
			driver.manage().deleteAllCookies();
			driver.get("https://www.amazon.com");
		}

		// We dont need to write the if-else conditions , we have assert in testng as
		// below for validations
		
		
		
		
		
		// We should always create independent test cases as below 
		
		@Test(priority = -1) // negative priority
		public void titleTest() {

			String title = driver.getTitle();
			System.out.println("page title :" + title);
			Assert.assertEquals(title,
					"Amazon.com. Spend less. Smile more.");

		}

		@Test(priority = 2)
		public void searchExistTest() {

			boolean flag = driver.findElement(By.id("twotabsearchtextbox")).isDisplayed();
			Assert.assertTrue(flag);

		}
		
		@Test(priority = 3)
		public void isHelpTest() {
			
			boolean flag = driver.findElement(By.linkText("Help")).isDisplayed();
			Assert.assertTrue(flag);

		}
		

		@AfterMethod
		public void teardown() {

			driver.quit();
		}
	

}
