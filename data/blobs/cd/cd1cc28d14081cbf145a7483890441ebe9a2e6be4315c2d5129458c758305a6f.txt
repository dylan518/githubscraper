package KeywordDrivern;

import java.io.IOException;
import java.time.Duration;

import org.apache.poi.EncryptedDocumentException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class baseTest {
   WebDriver driver;
   public void openBrowser() throws EncryptedDocumentException, IOException
   {
	   Flib flib = new Flib();
	  //read the data from proparty file
	  String browserValue = flib.readPropertyFile("./data/config.property","Browser");

	   //read the data from propertyFile(url)
	   String url = flib.readPropertyFile("./data/config.property","url");
	   //use the value of browser
	   if(browserValue.equalsIgnoreCase("chrome"))
	   {
		   System.setProperty("Webdriver.chrome.driver","./drivers/chromedriver.exe");
		    driver =new ChromeDriver();
		   driver.manage().window().maximize();
		   driver.get(url);
		   driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(15));
	   }
	   else if(browserValue.equalsIgnoreCase("fierfox"))
	   {
		   System.setProperty("Webdriver.gekco.driver","./drivers/geckodriver.exe");
		   driver=new FirefoxDriver();
		   driver.manage().window().maximize();
		   driver.get(url);
		   driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(15));
	   }
	   else
	   {
		   System.out.println("Enter the correct choice");
	   }
   }
   //method  to close the browser
   public void closeBrowser()
   {
	   driver.quit();
   }


}
