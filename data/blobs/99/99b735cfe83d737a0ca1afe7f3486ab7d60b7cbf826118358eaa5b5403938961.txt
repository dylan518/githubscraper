package TestCases;

import org.openqa.selenium.Alert;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.annotations.Test;



import PageObjects.LoginPage;
import PageObjects.LogoutPage;
import TestBase.BaseClass;

public class TC_001LoginTest extends BaseClass {

@Test(groups = {"sanity","master"})
public void verify_Login()
{
	 Log.info("***** starting TC_002LoginTest*****");
     try 
     {
	 LoginPage llp= new LoginPage(driver);
	 Log.info("click on makeappointment button");
	 llp.makeAppointment();
	 Log.info("enter username");
	 llp.userNAME(po.getProperty("USERNAME"));
	 Log.info("enter password");
     llp.passWORD(po.getProperty("PASSWORD"));
	 Log.info("click on login button");
	 llp.LOGIN1();
     Log.info("accept alert popup");
	 llp.acceptAlert();
	 Log.info("confirmation text is displayed or not");
     boolean loginhomepage=llp.makeAppointment1();
     LogoutPage lpp= new LogoutPage(driver);
	 Log.info("click on bars");
	 lpp.bars();	
	 Log.info("click on logout button");
	 lpp.logout();
     Assert.assertTrue(loginhomepage);
     // it if for failing test case
     //Assert.assertFalse(loginhomepage);  
     } 
     catch (Exception e) 
     {
 	 Log.info("test fails");
 	 Log.debug("debug Test logs...");
 	 Assert.fail();
 	 }
 	 Log.info("***** ending TC_002LoginTest*****");  

}
}