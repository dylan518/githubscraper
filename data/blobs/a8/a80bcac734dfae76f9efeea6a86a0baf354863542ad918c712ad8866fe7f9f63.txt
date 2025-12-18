package Gun07;

import Utils.BaseStaticDriver;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class Ornek3  extends BaseStaticDriver {
    public static void main(String[] args) {
        driver.get("https://www.facebook.com/");
        Bekle(2);

        WebElement yenihesap=driver.findElement(By.cssSelector("[id^='u_0_0_']"));
        yenihesap.click();
        Bekle(1);

        WebElement hesap=driver.findElement(By.name("firstname"));
        hesap.sendKeys("büşra");
Bekle(1);
        WebElement hesap2=driver.findElement(By.name("lastname"));
        hesap2.sendKeys("polat");
Bekle(1);
        WebElement reEmail=driver.findElement(By.name("reg_email_confirmation__"));
        Assert.assertFalse(reEmail.isDisplayed());
Bekle(1);
        WebElement email=driver.findElement(By.name("reg_email__"));
        email.sendKeys("onur@gmail.com");

        Assert.assertTrue(reEmail.isDisplayed());


        BekleKapat();
    }
}
