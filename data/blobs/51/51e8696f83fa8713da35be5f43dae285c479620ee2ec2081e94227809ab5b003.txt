package StepDefinitions;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.time.Duration;
import java.util.List;
import java.util.Properties;

import org.junit.Assert;
import org.junit.Before;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import PageObject.AddCustomer_obj;
import PageObject.Login_obj;
import PageObject.Pageobjectmanager;
import PageObject.Searchcustomerpage;
import Utilpackage.Utilityfile;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class Loginuser_SD 
{
	//need to create object since we need to use pageobject class 
	//methods here
	//the above two we need to use across all the below methods
	//they are global variables
	public WebDriver driver;
	public Login_obj login_page;
	public AddCustomer_obj Addcust;

	//public Login_obj login_page;
	//public AddCustomer_obj Addcust;
	public Searchcustomerpage searchpage;
	

	
	//public Pageobjectmanager pmo;

	//Utilityfile utilfilecontent;
	

	
	/*
	 * public Loginuser_SD(Utilityfile utilfilecontent) { //this refer to cuurent
	 * class this.utilfilecontent=utilfilecontent; }
	 */
	
	
	@Given("user launch chrome browser")
	public void user_launch_chrome_browser() throws FileNotFoundException 
	{	
		FileInputStream fis=new FileInputStream(System.getProperty("user.dir")+"//src//test//resources//global.properties");
		Properties prop=new Properties();
		try {
			prop.load(fis);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		String url = prop.getProperty("QAUrl");
		
		if(prop.getProperty("browser").equalsIgnoreCase("chrome"))
		{
		System.setProperty("webdriver.chrome.driver", "C:\\driver\\chromedriver.exe");
		driver=new ChromeDriver();
		driver.get(url);
		}
		else
		{
			System.out.println("different browser");
		}
		
		//utilfilecontent.driver=new ChromeDriver();
		//utilfilecontent.login_page = new Login_obj(utilfilecontent.driver);
		login_page = new Login_obj(driver);
		Addcust=new AddCustomer_obj(driver);
		
		 //pmo= new Pageobjectmanager(driver);
		//Login_obj login_page=pmo.LoginPage();
		
		 
		 
		searchpage =new Searchcustomerpage(driver);
	}
	


	//@When("user enter the {string} and {string}")
	//public void user_enter_the_and(String email, String password) 
	//{
		//login_page.enterEmail(email);
		//login_page.enterPassword(password);
	//}
	
	
	
	
	
	//REGULAR EXPRESSION (.+) 
	// Now in feature, it will work like username/"username"/"<username>"/p123/
	@When("^user enter the (.+) and (.+)$")
	public void user_enter_the_and(String email, String password) 
		{
		//utilfilecontent.login_page.enterEmail(email);
		//utilfilecontent.login_page.enterPassword(password);
		login_page.enterEmail(email);
		login_page.enterPassword(password);
		
		}
	
	@When("click on login button")
	public void click_on_login_button() 
	{
		//utilfilecontent.login_page.clickbutton();
		login_page.clickbutton();
	}

	@Then("user should be able to {string} title on Dashboard")
	public void user_should_be_able_to_heading_on_dashboard(String expectedtitle) 
	{
		//String actualtitle=utilfilecontent.driver.getTitle();
		String actualtitle=driver.getTitle();
		if(actualtitle.equalsIgnoreCase(expectedtitle))
		{
			Assert.assertTrue(true);
		}
		
		
	}

	
	/*
	 * DATA-DRIVEN TESTING
	 * 
	 * @When("user enter the details") public void
	 * user_enter_the_details(List<String> data) {
	 * //driver.findElement(By.id="name').sendkeys(data.get(0)); //this will take
	 * first index value from feature file - prathmesh Naik
	 * 
	 * System.out.println(data.get(0)); System.out.println(data.get(1));
	 * System.out.println(data.get(2)); System.out.println(data.get(3));
	 * 
	 * }
	 * 
	 * @When("click on submit button") public void click_on_submit_button() {
	 * System.out.println("logged in"); }
	 * 
	 * @Then("user should be successfully signed up") public void
	 * user_should_be_successfully_signed_up() {
	 * System.out.println("user signed up");
	 */
	
	
	@Then("user should not be able to login")
	public void user_should_not_be_able_to_login() {
	    System.out.print("user failed to login");
	}
	@Then("close the browser")
	public void close_the_browser()
	{

		//utilfilecontent.driver.close();
		driver.close();
	}
}
