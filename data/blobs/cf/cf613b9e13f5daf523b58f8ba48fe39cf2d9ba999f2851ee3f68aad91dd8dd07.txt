package testsuite;

import browserfactory.BaseTest;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

import java.util.List;

public class LoginTest extends BaseTest {

    String baseUrl = "https://www.saucedemo.com/";

    @Before
    public void setUp(){
     openBrowser(baseUrl);
    }

    @Test
    public void userShouldLoginSuccessfullyWithValidCredentials(){
//        Enter “standard_user” username
       driver.findElement(By.id("user-name")).sendKeys("standard_user");
//        * Enter “secret_sauce” password
        driver.findElement(By.id("password")).sendKeys("secret_sauce");
//        * Click on ‘LOGIN’ button
        driver.findElement(By.id("login-button")).click();
//        * Verify the text “PRODUCTS”
        String expectedMessage = "Products";
        WebElement actualTextElement = driver.findElement(By.xpath("//span[text()='Products']"));
        String actualMessage = actualTextElement.getText();
        Assert.assertEquals("Invalid Text", expectedMessage, actualMessage);

    }

    @Test
    public void verifyThatSixProductsAreDisplayedOnPage(){
//        Enter “standard_user” username
        driver.findElement(By.id("user-name")).sendKeys("standard_user");
//        * Enter “secret_sauce” password
        driver.findElement(By.id("password")).sendKeys("secret_sauce");
//        * Click on ‘LOGIN’ button
        driver.findElement(By.id("login-button")).click();
//        Verify that six products are displayed on page
        int expectedNumbers = 6;
        List <WebElement> actualElements =  driver.findElements(By.className("inventory_item"));
        int actualNumbers = actualElements.size();
        Assert.assertEquals("Doesn't match", expectedNumbers,actualNumbers);
    }

    @After
    public void tearDown(){
    closeBrowser();
    }
}
