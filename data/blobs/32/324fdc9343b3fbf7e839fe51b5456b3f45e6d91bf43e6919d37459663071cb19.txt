package selenium.com.blaze.pages;

import com.beust.ah.A;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.testng.Assert;
import selenium.utils.BrowserUtils;

public class ProductInfoPage {
    public ProductInfoPage(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    @FindBy(xpath = "//a[.='Add to cart']")
    WebElement addCart;
    @FindBy(css = "a[id='cartur']")
    WebElement cartButton;
    @FindBy(xpath = "//h2")
    WebElement header;
    @FindBy(xpath = "//h3")
    WebElement price;

    public void validateHeader() {
        Assert.assertEquals(BrowserUtils.getText(header), "MacBook Pro");
        Assert.assertTrue(price.isDisplayed());
    }

    public void addTocartButton(WebDriver driver) throws InterruptedException {
        addCart.click();


        Thread.sleep(3000);
        String actual = BrowserUtils.alertGetText(driver);
        String expected = "Product added";
        Assert.assertEquals(actual, expected, "Failed to validate");
        BrowserUtils.acceptAlert(driver);
        cartButton.click();


    }

}
