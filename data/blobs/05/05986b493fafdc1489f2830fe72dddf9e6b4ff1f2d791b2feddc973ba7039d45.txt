package com.workflow.StepDef;

import com.workflow.Pages.HomePage;
import io.cucumber.java.en.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class StepDefinitions {
    WebDriver driver = new ChromeDriver();
    HomePage homePage = new HomePage();

    @Given("I am on the Amazon home page")
    public void i_am_on_the_amazon_home_page(){
        driver.get("https://www.amazon.com");
    }

    @When("I search for a product")
    public void i_search_for_a_product(){
        String productName = "Realme C15";
        homePage.searchForProduct(productName);
    }

}
