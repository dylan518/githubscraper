package registerSuiteTests;

import org.testng.Assert;
import org.testng.annotations.Test;
import registerDataSuite.InvalidPasswordData;
import homePage.HomePage;

import java.io.IOException;
import java.text.ParseException;

public class RegisterWithInvalidPassword extends TestBase{
    HomePage homePage;
    registerSuite.RegisterWithInvalidPassword registerPage;
    String currentTime = String.valueOf(System.currentTimeMillis());

    @Test
    public void navigateToRegisterPage(){
        homePage = new HomePage(driver);
        homePage.navigateToRegisterPage();

    }

    @Test(priority = 1)
    public void enterRegisterData() throws IOException, ParseException, org.json.simple.parser.ParseException {
        InvalidPasswordData data = new InvalidPasswordData();
        data.registerData();
        registerPage = new registerSuite.RegisterWithInvalidPassword(driver);
        registerPage.enterRegisterData(data.firstName, data.lastName, data.email+currentTime+"@gmail.com", data.telephone, data.password);
        Assert.assertEquals(registerPage.getErrorMessage(),"Password must be between 4 and 20 characters!");

    }
}
