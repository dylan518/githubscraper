package TestCase;

import java.io.File;
import java.io.IOException;

import org.codehaus.plexus.util.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.testng.annotations.Test;

import PageObject.AddCustomer;
import PageObject.LoginPage;

public class TC_02_AddCustomer extends BaseClass{
	
	@Test
	public void addCustomer() throws InterruptedException, IOException
	{
		driver.get(baseURLBS);
		lp=new LoginPage(driver);
		lp.setUsername(usernameBS);
		lp.setPassword(passwordBS);
		lp.clickLoginButton();
		Thread.sleep(2000);
		 ad=new AddCustomer(driver);
//		Add Customner
		ad.clickNewCustomer();
		Thread.sleep(5000);
		ad.setCustomerName("Patatik");
		ad.selectGender();
		ad.setDAte("12/12/1998");
		ad.setAddress("Waghave");
		ad.setCity("Kolhapur");
		ad.setState("MAHARASHTRA");
		ad.setPin("416230");
		ad.setMobile("7744558899");
		ad.setEmail(generateEmail());
		ad.password("12345678");
		ad.clickSaveButton();
		Thread.sleep(3000);
		TakesScreenshot ts=(TakesScreenshot)driver;
		File src=ts.getScreenshotAs(OutputType.FILE);
		File trc=new File(".//Sc//pm.png");
		FileUtils.copyFile(src, trc);
		Thread.sleep(3000);
		lp.clickLogoutButton();
		driver.switchTo().alert().accept();
		logger.info("Test Case Passed");
	}
	
}
