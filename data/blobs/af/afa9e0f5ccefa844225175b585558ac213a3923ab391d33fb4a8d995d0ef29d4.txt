package seleniumSessionTest;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class WebDriverLunch {

	public static void main(String[] args) {
		ChromeOptions co = new ChromeOptions();
		co.addArguments("--remote-allow-origins=*");
		System.setProperty("webdriver.chrome.driver", "/Users/viveksingh/Documents/drivers/chromedriver");
		WebDriver driver = new ChromeDriver(co);

		driver = null;

		driver = new ChromeDriver(co);
		driver = new ChromeDriver(co);

		driver.get("https:google.com");

		driver.quit();
	}

}
