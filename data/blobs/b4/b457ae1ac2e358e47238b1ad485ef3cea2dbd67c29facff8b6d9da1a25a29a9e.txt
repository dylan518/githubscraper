package Pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class HomePage extends MainPage {

    public HomePage(WebDriver driver) {
        super(driver);
    }

    @FindBy (xpath = "img[src='/_resources/themes/orangehrm/dist/images/OrangeHRM_Logo.svg']")
    private WebElement logoButton;

    @FindBy (xpath = "//a[normalize-space()='EN']")
    private WebElement languageEnglishButton;

    @FindBy (xpath = "//a[normalize-space()='ES']")
    private WebElement languageSpanishButton;

    @FindBy (xpath = "//a[@class='nav-link-hed'][normalize-space()='Solutions']")
    WebElement solutionsButton;

    @FindBy (xpath = "//a[@class='nav-link-hed'][normalize-space()='Why OrangeHRM']")
    private WebElement whyButton;

    @FindBy (xpath = "//a[@class='nav-link-hed'][normalize-space()='Resources']")
    private WebElement resourcesButton;

    @FindBy (xpath = "//a[@class='nav-link-hed'][normalize-space()='Company']")
    private WebElement companyButton;

    @FindBy (xpath = "//div[@class='d-flex web-menu-btn']//li[1]//a[1]")
    private WebElement bookDemoButton;

    @FindBy (xpath = "//body/nav[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]/button[1]")
    private WebElement contactSalesButton;

    @FindBy (id = "Form_submitForm_EmailHomePage")
    private WebElement enterEmailInput;

    @FindBy(id = "Form_submitForm_action_request")
    private WebElement freeTrialButton;

//    public void clickLogo(){
//        logoButton.click();
//    }
//
//    public void setLanguageEnglish(){
//        languageEnglishButton.click();
//    }
//
//    public void setLanguageSpanish(){
//        languageSpanishButton.click();
//    }
//
//    public void clickSolutionsButton(){
//        solutionsButton.click();
//    }

    public void clickBookDemo(){
        bookDemoButton.click();
    }

    public void clickContactSales(){
        contactSalesButton.click();
    }

    public void enterEmail(){
        enterEmailInput.sendKeys("mail@mail.com");
   }

   public void clickFreeTrialButton(){
        freeTrialButton.click();
   }

}
