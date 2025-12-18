package ecomm.Tests;

import java.io.IOException;

import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import ecomm.BaseActions;
import ecomm.pages.SignUpPage;

public class SignUpTest extends BaseActions {
	
	SignUpPage signupPage;
	
	@BeforeTest
	public void BrowserLaunch() throws IOException
	{
		init_Driver();
		getDriver().get(properties.getProperty("AppUrl"));
	}
	
	@Test(dataProvider="getSignUpData")
	public void userSingup(String CustomerFirstname, String CustomerLastname, String Password, String Firstname,
			String Lastname, String Company,String Address, String City, String State, String Postcode, String Country, String Phone, String Alias) throws Exception
	{
		signupPage = new SignUpPage(getDriver());
		signupPage.SingUp().click();
		//signupPage.emailAddress("qauser3@aol.com");
		signupPage.CreateEmailAddress();
		signupPage.createaccount().click();
		Thread.sleep(3000);
		signupPage.gender().click();
		signupPage.UserSignUp(CustomerFirstname, CustomerLastname, Password, Firstname, Lastname, Company, Address, City, State, Postcode, Country, Phone, Alias);
	    signupPage.submit().click();
	}
	
	@AfterTest
	public void quitBrowser()
	{
		//getDriver().quit();
	}
	
	@DataProvider
	public String [][] getSignUpData(){		
		String [][] dataRecords = getData("SignUpData.xlsx","Sheet1");
		return dataRecords;
	}

}
