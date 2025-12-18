package SelPackage;

import java.time.Duration;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.NoAlertPresentException;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AutomationPractice {

//Tests to see if content is present on a site
	public static String contentTest() {
		String myString;
		// Web Driver Path
		System.setProperty("webdriver.chrome.driver", "D:\\ChromeDriver\\chromedriver.exe");

		// Objects Initiated and Max Screen Arg
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--start-maximized");
		WebDriver driver = new ChromeDriver(options);

		driver.navigate().to("https://the-internet.herokuapp.com");

		try {		
			// Wait for item avalibilty
			WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
			wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//*[contains(text(), 'Welcome')]")));

			myString = "Passed";

		} catch (TimeoutException e) {
			myString = "Failed";
			
		} finally {
			driver.quit();
			
		}

		return myString;
	}

//Tests to see if a sites authentication functionality
	public static String authTest() {

		// Web Driver Path
		System.setProperty("webdriver.chrome.driver", "D:\\ChromeDriver\\chromedriver.exe");

		// Objects Initiated and Max Screen Arg
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--start-maximized");
		WebDriver driver = new ChromeDriver(options);

		// Sample Web Site Load with Embedded Credentials for Basic Auth
		String basicAuthUrl = "https://admin:admin@the-internet.herokuapp.com/basic_auth";

		// Navigate to the page with Basic Auth
		driver.navigate().to(basicAuthUrl);

		// Get Text For Confirmed Auth
		String myString = driver.findElement(By.cssSelector("p")).getText();

		// Test Logic
		if (myString.equals("Congratulations! You must have the proper credentials.")) {
			myString = "Passed";
		} else {
			myString = "Failed";
		}

		// Quit and Exit
		driver.quit();
		return myString;
	}

//Tests to see if context Menu is Present
	public static String contextMenuTest() {
		// Return String
		String myString;

		// Web Driver Path
		System.setProperty("webdriver.chrome.driver", "D:\\ChromeDriver\\chromedriver.exe");

		// Objects Initiated and Max Screen Arg
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--start-maximized");
		WebDriver driver = new ChromeDriver(options);

		driver.navigate().to("https://the-internet.herokuapp.com/context_menu");

		// Find and Store Element
		WebElement element = driver.findElement(By.id("hot-spot"));

		// Action Object
		Actions action = new Actions(driver);

		// Right Click
		action.contextClick(element).perform();

		// Is the Alert Present
		try {
			Alert alert = new WebDriverWait(driver, Duration.ofSeconds(5)).until(ExpectedConditions.alertIsPresent());
			myString = "Passed";
			alert.accept();

		} catch (NoAlertPresentException e) {
			myString = "Failed";

		} finally {
			driver.quit();

		}

		return myString;
	}
}
