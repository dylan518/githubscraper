package com.navfort.pages;

import com.navfort.utilities.ConfigurationReader;
import com.navfort.utilities.Driver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {
    public LoginPage(){
        PageFactory.initElements(Driver.getDriver(),this);
    }
    @FindBy(id = "prependedInput")
    private WebElement usernameField;

    @FindBy(id = "prependedInput2")
    private WebElement passwordField;

    @FindBy(id = "_submit")
    private WebElement loginBtn;

    @FindBy(xpath = "//h2[@class='title']")
    public WebElement loginPageTitle;

    @FindBy (id="remember_me")
    public WebElement rememberMeCheckBox;

    @FindBy (xpath = "//a[@href='/user/reset-request']")
    public WebElement forgotPasswordLink;


    public void loginAsUserType(String userType){

        String password = "";
        String username = "";

        if (userType.equalsIgnoreCase("driver")) {
            username = ConfigurationReader.getProperty("driver_username");
            password = ConfigurationReader.getProperty("driver_password");
        }
        else if (userType.equalsIgnoreCase("sales manager")) {
            username = ConfigurationReader.getProperty("sales_manager_username");
            password = ConfigurationReader.getProperty("sales_manager_password");
        }
        else if (userType.equalsIgnoreCase("store manager")) {
            username = ConfigurationReader.getProperty("store_manager_username");
            password = ConfigurationReader.getProperty("store_manager_password");
        }

        usernameField.sendKeys(username);
        passwordField.sendKeys(password);
        loginBtn.click();
    }

    public void loginAsDriver(){
        String username = ConfigurationReader.getProperty("driver_username");
        String password = ConfigurationReader.getProperty("driver_password");

        usernameField.sendKeys(username);
        passwordField.sendKeys(password);
        loginBtn.click();
    }

    public void loginAsSalesManager(){
        String username = ConfigurationReader.getProperty("sales_manager_username");
        String password = ConfigurationReader.getProperty("sales_manager_password");

        usernameField.sendKeys(username);
        passwordField.sendKeys(password);
        loginBtn.click();
    }

    public void loginAsStoreManager(){
        String username = ConfigurationReader.getProperty("store_manager_username");
        String password = ConfigurationReader.getProperty("store_manager_password");

        usernameField.sendKeys(username);
        passwordField.sendKeys(password);
        loginBtn.click();
    }


}
