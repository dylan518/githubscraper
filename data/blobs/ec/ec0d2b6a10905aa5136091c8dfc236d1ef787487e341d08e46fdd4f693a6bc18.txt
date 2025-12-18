package KateaManoila;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class App {
    private static  ChromeDriver driver;

    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "drivers/chromedriver");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://demoqa.com/");
        WebElement header = driver.findElement(By.tagName("header"));
        WebElement consentButton = driver.findElement(By.cssSelector(".fc-button.fc-cta-consent.fc-primary-button"));
        consentButton.click();
//        WebElement elementsCard = driver.findElement(By.xpath("(//div[@class='card mt-4 top-card'])[1]"));
//        elementsCard.click();
        WebElement elements=getCard("Elements");
        elements.click();
        Thread.sleep(2000);
        WebElement textBox=driver.findElement(By.id("item-0"));
        textBox.click();


        String currentUrl = driver.getCurrentUrl();
        System.out.println(currentUrl);
        WebElement nameField = driver.findElement(By.id("userName"));
        nameField.sendKeys("Ana");
        WebElement userEmail = driver.findElement(By.id("userEmail"));
        userEmail.sendKeys("test@test.com");
        WebElement currentAddress = driver.findElement(By.id("currentAddress"));
        currentAddress.sendKeys("Iasi");
        WebElement permanentAddress = driver.findElement(By.xpath("//textarea[@id='permanentAddress']"));
        permanentAddress.sendKeys("Basarabia");
        WebElement submit = driver.findElement(By.id("submit"));
        submit.click();
        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].scrollIntoView(true);", submit);
        Thread.sleep(5000);


        WebElement nameResult = driver.findElement(By.id("name"));
        String nameDisplayed = String.valueOf(nameResult.getText());
        System.out.println(nameDisplayed);

        WebElement emailResult = driver.findElement(By.id("email"));
        String emailDisplayed =String.valueOf(emailResult.getText());
        System.out.println(emailDisplayed);

        WebElement currentAddressResult = driver.findElement(By.xpath("//p[@id='currentAddress']"));
        String displayedCurrentAddress = String.valueOf(currentAddressResult.getText());
        System.out.println(displayedCurrentAddress);

        WebElement permanentAddressResult = driver.findElement(By.xpath("//p[@id='permanentAddress']"));
        String displayedPermanentAddress =String.valueOf(permanentAddressResult.getText());
        System.out.println(displayedPermanentAddress);




        //       clickHeaderTestCase(header);
        driver.quit();



    }
    private static WebElement getCard(String card){
        return driver.findElement(By.xpath("//h5[text()='" + card +"'] //ancestor::div[@class='card mt-4 top-card']"));

    }

    private static void clickHeaderTestCase(WebElement header) {
        header.click();
    }


}
