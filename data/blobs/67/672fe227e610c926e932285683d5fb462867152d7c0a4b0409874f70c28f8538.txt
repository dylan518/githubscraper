package management_on_schools.pages.Sema03_07_16;

import management_on_schools.utilities.Driver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class US_03_07_16 {
    public US_03_07_16() {
        PageFactory.initElements(Driver.getDriver(), this);
    }

    @FindBy(xpath = "//div[text()='Contact Message Created Successfully']")
    public WebElement verifyMessage;

    @FindBy(xpath = "//*[@id='email']")
    public WebElement eMail;

    @FindBy(xpath = "(//*[text()='Required'])[1]")
    public WebElement requiredName;

    @FindBy(xpath = "//div[text()='Please enter valid email']")
    public WebElement alertEmail;

    @FindBy(xpath = "//a[text()='Contact Get All']")
    public WebElement contacts;

    @FindBy(xpath = "//h5[@bg='primary']")
    public WebElement contactMessages;








}


