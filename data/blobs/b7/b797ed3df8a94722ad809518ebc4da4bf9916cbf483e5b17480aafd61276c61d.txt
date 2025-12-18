package test;

import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;
import pageobject.CustomerLoginPage;
import pageobject.HomePage;
import pageobject.MyAccountPage;
import testcase.WebTest;

public class CustomerLoginTest extends WebTest {

    public HomePage homePage;
    public CustomerLoginPage customerLoginPage;
    public MyAccountPage myAccountPage;

    CustomerLoginTest() { //why called or used
        super();
    }

    @BeforeMethod
    public void beforeMethod(){ //defined method
        initialization();//called initi method
        homePage = new HomePage();
        customerLoginPage = new CustomerLoginPage();
        myAccountPage = new MyAccountPage();
    }

    @Test
    public void verifySignInWithValidEmail(){
        SoftAssert softAssert = new SoftAssert();//use of it
        homePage.clickOnSignInBtn(); //kha se aya bhi tu???
        customerLoginPage.login(prop.getProperty("username"),prop.getProperty("password"));
        softAssert.assertEquals(myAccountPage.textOfElement(),"Welcome, lakshya sharma!","title must match for element");
        softAssert.assertEquals(myAccountPage.textOfElement2(),"My Account","title must match for element2");
        softAssert.assertAll();
    }

    //@Test
   // public void

    @AfterMethod
    public void afterMethod() throws InterruptedException {
        Thread.sleep(5000);
        //driver.close();
    }
}
