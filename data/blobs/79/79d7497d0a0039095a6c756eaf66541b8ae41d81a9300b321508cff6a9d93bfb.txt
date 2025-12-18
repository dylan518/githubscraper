package pageobjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class SignInPage {
	WebDriver driver;
	
	
	public SignInPage(WebDriver driver) {
		this.driver=driver;
		
		PageFactory.initElements(driver, this);
	}
	@FindBy(xpath="//ul[@class='links']//a[contains(text(),'Sign in')]")
	private WebElement clickOnSign;
	
	@FindBy(xpath="//input[@id='email']")
	private WebElement emailText;
	
	@FindBy(xpath="//input[@id='password']")
	private WebElement PassText;
	
	@FindBy(xpath="//button[@id='btn-submit']")
	private WebElement clickOnSubmit;
	
	public WebElement clickOnSignInLink() {
		return clickOnSign;
	}
	public WebElement passEmail() {
		return emailText;
	}
	public WebElement paasPassword() {
		return PassText;
	}
	public WebElement clickSubmit() {
		return clickOnSubmit;
	}
	

}
