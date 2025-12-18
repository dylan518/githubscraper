package selenium;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class ChromeBrowser {
	
	static WebDriver driver;

	public static void main(String[] args) throws InterruptedException {
		
	driver = new ChromeDriver();
	Thread.sleep(3000);
	driver.manage().window().maximize();
	Thread.sleep(3000);
	driver.quit();
//	driver.close();
	
	// driver.manage().window().minimize();
	}

}
