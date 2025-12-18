package TestsCases;

import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import Pages.AccountSuccesPage;
import Pages.LandingPage;
import Pages.RegisterPage;
import TestBase.TestBase;
import Utulities.Util; 


public class RegisterTest extends TestBase{

	public RegisterTest() throws Exception {
		super();
		
	}
	
	public WebDriver driver;
	public LandingPage landingpage;
	public RegisterPage registerpage;
	public AccountSuccesPage accountsuccespage;
	
	//setup browser
	@BeforeMethod
	public void launchURL() {
		driver = initializeBrowserAndOpenApplication(prop.getProperty("browser"));
		landingpage = new LandingPage(driver);
		
		
	}
	
	
	// register with all detail (valid email)
	@Test(priority=1)
public void verifyRegisterWithAllDetail() {
	landingpage.clickOnMyAccountDropDown();
		registerpage=landingpage.selectRegisterOption();
	accountsuccespage = registerpage.registerPageAllDetails(dataprop.getProperty("firstname"), dataprop.getProperty("lastname"), 
				Util.emailWithDateTimeStamp(), dataprop.getProperty("telephone"),dataprop.getProperty("password"), 
				dataprop.getProperty("confirmPassword"));
		Assert.assertTrue(accountsuccespage.displayStatutsAccountCreatedSuccessfulltMessage());
	}
	
	
	//register with existing Email
	@Test(priority=2,enabled=false)
	public void verifyRegisterWithExistingEmail() {
		landingpage.clickOnMyAccountDropDown();
        registerpage=landingpage.selectRegisterOption();
registerpage.registerPageAllDetails(dataprop.getProperty("firstname"), dataprop.getProperty("lastname"), 
				dataprop.getProperty("email"), dataprop.getProperty("telephone"),dataprop.getProperty("password"), 
				dataprop.getProperty("confirmPassword"));
		Assert.assertTrue(registerpage.retrieveTextofDuplicateEmail().contains(dataprop.getProperty("emailExistWaringMessage")));
		
	}
	
	// register with no Details 
	@Test(priority=3 ,enabled=false)
public void verifyRegisterWithNoDetails() {
		landingpage.clickOnMyAccountDropDown();
        registerpage=landingpage.selectRegisterOption();
		registerpage.clickOnContinueButton();
		Assert.assertTrue(registerpage.retriveAllWarninMessage(dataprop.getProperty("policyWarningMessage"), dataprop.getProperty("firstNameWarningMessage"), dataprop.getProperty("lastNameWarningMessage"),
				dataprop.getProperty("emailWarningMessage"), dataprop.getProperty("telephoneWarningMessage"), dataprop.getProperty("passwordWarningMessage")));
	}
	
	//close browser
	
	@AfterMethod
	public void tearDown() {
		driver.quit();
	}
	

}
