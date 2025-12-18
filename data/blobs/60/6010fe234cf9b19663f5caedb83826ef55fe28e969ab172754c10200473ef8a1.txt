package Pages.Widgets;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class Tabs {

    public final String url = "https://demoqa.com/tabs";
    public WebDriver driver;

    public Tabs(WebDriver driver) {
        this.driver = driver;
    }

    public By tabWhat = By.id("demo-tab-what");
    public By whatText = By.id("demo-tabpane-what");
    public By tabOrigin = By.id("demo-tab-origin");
    public By originText = By.id("demo-tabpane-origin");
    public By tabUse = By.id("demo-tab-use");
    public By useText = By.id("demo-tabpane-use");

    public WebElement getTabWhat() {
        return driver.findElement(tabWhat);
    }

    public WebElement getWhatText() {
        return driver.findElement(whatText);
    }

    public WebElement getTabOrigin() {
        return driver.findElement(tabOrigin);
    }

    public WebElement getOriginText() {
        return driver.findElement(originText);
    }

    public WebElement getTabUse() {
        return driver.findElement(tabUse);
    }

    public WebElement getUseText() {
        return driver.findElement(useText);
    }
}
