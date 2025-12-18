package selenium_webdriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class Screenshot {

	public static void main(String[] args) throws Exception {


		WebDriverManager.chromedriver().setup();
		WebDriver driver = new ChromeDriver();
		
		driver.get("https://www.instagram.com/accounts/login/");
		driver.manage().window().maximize();
		Thread.sleep(3000);
		
		WebElement txt_username=driver.findElement(By.name("username"));
		txt_username.sendKeys("cristiano");
		
		WebElement txt_pass = driver.findElement(By.name("password"));
		txt_pass.sendKeys("wdfj7937");
		
		WebElement btn_login= driver.findElement(By.xpath("//button[text()='Log In']"));
		btn_login.click();
		
	}

}
