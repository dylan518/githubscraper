package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class WishqueHome extends BasePage {
    public WishqueHome(WebDriver driver) {
        super(driver);
    }

    @FindBy(xpath = "//input[@id='search_query']")
    public WebElement txtInputField;

    @FindBy(xpath = "//a[@id='search_query_button']")
    public WebElement btnSearch;

    @FindBy(xpath = "//img[@alt='Fresh Flowers']")
    public WebElement freshFlowers;

    public void typeInSearchBox(String txtValue){
        txtInputField.sendKeys(txtValue);
    }

    public <T> T clickSearchButton(String pageType) {
        btnSearch.click();
        if (pageType.equals("cakes")){
            return (T)PageFactory.initElements(driver, CakePage.class);
        }else{
            return (T)PageFactory.initElements(driver, PerfumePage.class);
        }
    }

    public <T> T clickFreshFlowers() {
        freshFlowers.click();
        return (T) PageFactory.initElements(driver, FreshFlowerPage.class);
    }


}
