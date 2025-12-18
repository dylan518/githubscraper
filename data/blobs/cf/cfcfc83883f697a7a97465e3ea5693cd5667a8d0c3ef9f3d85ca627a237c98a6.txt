package SeleniumPackage;

import SeleniumPackage.Utilities.BaseDriver;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class _27_Wait2 extends BaseDriver {
    @Test
    public void Test(){
        driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-use-explicit-wait-in-selenium.html");

        //click edilecek nesneyi bulduk
        WebElement clickMe = driver.findElement(By.xpath("//button[.='Click me to start timer']"));
        //click ettik.
        clickMe.click();

        //wait sınıfından nesne türettik ve kullanıcaz.
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));

        //wait nesnesini kullandık ve içersinde bekleteceğimiz elementin locatorunu verdik ve o locatordeki text şu olana kdar bekle dedik.

        wait.until(ExpectedConditions.textToBe(By.id("demo"),"Selenium"));

        //Doğrulama yapacağımız textin elementini ekranda bulduk.
        WebElement seleniumCheck = driver.findElement(By.id("demo"));
        //elementin text'ini string değişkene attım.
        String seleniumText = seleniumCheck.getText().toLowerCase();
        //Doğrulama
        //bool ifadeye bak string seleniumText değişkeni eşitse "selenium" değerine test başarılı eğer eşit değilse "text'ler eşleşmedi" uyarısı ekrana basılır.
        Assert.assertTrue("text'ler eşleşmedi",seleniumText.equals("selenium"));


        WaitAndClose();
    }

}
