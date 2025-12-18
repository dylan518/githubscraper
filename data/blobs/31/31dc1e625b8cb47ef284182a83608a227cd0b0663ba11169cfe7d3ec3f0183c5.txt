package org.adactinpojo;

import org.baseclass.BaseClass;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class AdactinHotelLoginPojo1 extends BaseClass {
	
	public AdactinHotelLoginPojo1(){
	PageFactory.initElements(driver, this);	
	}

	@FindBy(id="username")
	public WebElement emailText;
	
	@FindBy(id="password")
	public WebElement passwordText;
	
	@FindBy(id="login")
	public WebElement login;

	public WebElement getEmailText() {
		return emailText;
	}

	public WebElement getPasswordText() {
		return passwordText;
	}

	public WebElement getLogin() {
		return login;
	}
	
	
}
