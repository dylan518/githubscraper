package com.provectus.tests;

import com.provectus.DataSource;
import com.provectus.components.Header;
import com.provectus.pages.MainPage;
import com.provectus.pages.SignInPage;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

import static com.codeborne.selenide.Selenide.open;

public class LoginTest extends BaseTest{

    @Test
    public void successfulLoginTest() throws IOException {

        open("");
        MainPage mainPage = new MainPage();

        File file = new File("src/main/resources/feedback_EN.properties");
        Properties properties = new Properties();
        properties.load(new FileReader(file));
        Assert.assertEquals(mainPage.getWelcomeMessageText(), properties.getProperty("welcomeMessageHome"), "The welcome messages text should be the same");

        Header header = new Header();
        SignInPage signInPage = header.goToSignInPage();
        Assert.assertEquals(signInPage.getWelcomeMessage(), properties.getProperty("welcomeMessageSignIn"), "The welcome messages text should be the same");

        signInPage.signIn(properties.getProperty("email"), properties.getProperty("password"));

        Assert.assertTrue(!header.getRegisterLink().isDisplayed());
        Assert.assertTrue(!header.getLogInLink().isDisplayed());
        Assert.assertTrue(header.getLogoutLink().isDisplayed());
        Assert.assertTrue(header.getMyAccountLink().isDisplayed());
    }
}
