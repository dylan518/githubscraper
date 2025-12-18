package Pages;

import Core.AppiumBase;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.testng.Assert;

public class LoginPage extends AppiumBase {
    @FindBy(xpath = "//android.widget.AutoCompleteTextView[@resource-id=\"com.banggood.client:id/et_email\"]")
    private WebElement email;
    @FindBy(xpath = "//android.widget.EditText[@resource-id=\"com.banggood.client:id/et_pwd\"]")
    private WebElement password;
    @FindBy(xpath = "//android.widget.Button[@resource-id=\"com.banggood.client:id/btn_sign_in\"]")
    private WebElement signInButton;

    public LoginPage() {
        PageFactory.initElements(new AppiumFieldDecorator(androidDriver), this);
    }

    public boolean verifyLoginScreenDisplayEmail() {
        try {
            webDriverWait.until(ExpectedConditions.visibilityOf(email));
            Assert.assertTrue(email.isDisplayed());
            System.out.println(email.getText() + ": is displayed");

            System.out.println("===================");
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public boolean verifyLoginScreenDisplayPassword() {
        try {
            webDriverWait.until(ExpectedConditions.visibilityOf(password));
            Assert.assertTrue(password.isDisplayed());
            System.out.println(password.getText() + ": is displayed");

            System.out.println("===================");
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public boolean verifyLoginScreenDisplaySignInButton() {
        try {
            webDriverWait.until(ExpectedConditions.visibilityOf(signInButton));
            Assert.assertTrue(signInButton.isDisplayed());
            System.out.println(signInButton.getText() + " Button: is displayed");

            System.out.println("===================");
            return true;
        } catch (Exception e) {
            return false;
        }
    }


}
