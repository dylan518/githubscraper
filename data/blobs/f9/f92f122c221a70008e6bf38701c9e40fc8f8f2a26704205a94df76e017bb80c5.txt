package test_scripts;

import org.openqa.selenium.WebDriver;
import org.testng.annotations.Test;

import pages.Category;
import pages.HomePage;
import pages.SignUp_Login;
import utils.Driver_setup;

public class View_women_category_products 
{
	WebDriver driver;
	@Test
	public void women_category_products() 
	    {
		  driver = Driver_setup.launch_Browser();
		  HomePage hp = new HomePage();
		  hp.navigate_to_magento_link(driver);
		  hp.homepage_displayed(driver);
		  
		  SignUp_Login sln = new SignUp_Login();
		  sln.enter_correct_cred(driver);
		  
		  Category c = new Category();
		  c.W_cat_click(driver);
		  c.Verify_women_category_page_visible(driver);
         }
  }