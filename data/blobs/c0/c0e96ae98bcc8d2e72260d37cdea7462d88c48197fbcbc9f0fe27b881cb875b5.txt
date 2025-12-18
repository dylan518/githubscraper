package com.way2automation.pages;/*
 *Vinay Creation
 *Date of Creation
 */

import com.way2automation.utility.Utility;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.testng.Reporter;


public class CustomerPage extends Utility {

    private static final Logger log = LogManager.getLogger(CustomerPage.class.getName());
    //location of elements
//    By searchCustomerField = By.xpath("//input[@placeholder='Search Customer']");
//    By deleteBtn  = By.xpath("//button[contains(text(),'Delete')]");

    @FindBy(xpath = "//input[@placeholder='Search Customer']")
    WebElement _serchCustomerField;

    @FindBy(xpath = "//button[contains(text(),'Delete')]")
    WebElement _deleteBtn;


    //actions performed on elements
    public void searchCustomerName(String customerName) {
        Reporter.log("Search customer Name :" + customerName + "customer name field " + _serchCustomerField.toString() + "<br>");
        sendTextToElement(_serchCustomerField, customerName);
        log.info("Search customer Name :" + customerName + "customer name field " + _serchCustomerField.toString());
    }

    public void clickOnDeleteButton() {
        Reporter.log("Clicking on delete button : " + _deleteBtn.toString());
        clickOnElement(_deleteBtn);
    }

}
