package com.AcharyaUniversity_ERP.Testcase;

import org.testng.annotations.Test;
import org.testng.annotations.Test;

import com.AcharyaUniversity_ERP.Pageobject.LoginFunctionalitypage_University;
import com.AcharyaUniversity_ERP.Utility.Readconfig;

public class LoginFunctionality_Univesity_Test extends BaseClass_University
{
	Readconfig read = new Readconfig();
	LoginFunctionalitypage_University login; 


	
	@Test
	public void logintes() throws InterruptedException
	{
        
		login = new LoginFunctionalitypage_University(driver);
		
		login.visitsite();

		login.username();

		log.info("username is passed");

		login.password();

		log.info("password is passed");

		login.Login();

		log.info("clicked on login");

		/*String str = driver.getCurrentUrl();

		Assert.assertEquals(str, "https://8c68-2401-4900-1f26-22f-7803-766e-9a5d-ab57.ngrok-free.app/Dashboard");

		log.info("home page is displayed");*/
	}
}