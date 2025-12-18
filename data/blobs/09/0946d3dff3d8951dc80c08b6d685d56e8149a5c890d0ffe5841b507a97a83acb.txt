package com.cydeo.step_definitions;

import com.cydeo.pages.Vytrack_Login_Page;
import com.cydeo.utilities.BrowserUtils;
import com.cydeo.utilities.ConfigurationReader;
import com.cydeo.utilities.Driver;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;

import java.util.Map;

public class Vytrack_Loging_Step_Def_OfficeHours {
    Vytrack_Login_Page loginPage=new Vytrack_Login_Page();

    @Given("user is on the login page")
    public void user_is_on_the_login_page() {
        Driver.getDriver().get(ConfigurationReader.getProperty("Vytrack_env"));

    }
    @When("user enter below credentials")
    public void user_enter_below_credentials(Map<String,String> credentials) {
        loginPage.login(credentials.get("username"),credentials.get("password"));

    }
//    @Then("user should be able to login as below")
//    public void userShouldBeAbleToLoginAsBelow(String name) {
//        System.out.println("name = " + name);
//    }

    @When("user enters the driver information")
    public void user_enters_the_driver_information() {
        String username = ConfigurationReader.getProperty("driver_username");
        String password = ConfigurationReader.getProperty("vytrack_password");

        loginPage.login(username,password);

    }
    @Then("user should be able to login")
    public void user_should_be_able_to_login() {
        BrowserUtils.waitFor(10);
        String actualTitle = Driver.getDriver().getTitle();
        String expectedTitle = "Dashboard";


        Assert.assertEquals(expectedTitle,actualTitle);

    }

    @When("user enters the sales manager information")
    public void user_enters_the_sales_manager_information() {
        String username = ConfigurationReader.getProperty("sales_manager_username");
        String password = ConfigurationReader.getProperty("sales_manager_password");

        loginPage.login(username,password);



    }

    @When("user enters the store manager information")
    public void user_enters_the_store_manager_information() {
        String username = ConfigurationReader.getProperty("store_manager_username");
        String password = ConfigurationReader.getProperty("store_manager_password");

        loginPage.login(username,password);
    }}

