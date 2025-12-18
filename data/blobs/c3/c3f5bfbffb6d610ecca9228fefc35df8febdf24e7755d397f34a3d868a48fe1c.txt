package web_element_test;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.Test;

public class Actions_FileUpload {
    WebDriver driver;

    @BeforeSuite
    public void startUp() throws Exception {

        WebDriverManager.chromedriver().setup();

        driver = new ChromeDriver();

        driver.get("https://demo.guru99.com/test/upload/");
        driver.manage().window().maximize();
        Thread.sleep(5000);

        System.out.println("Website opened");
    }

    @Test
    public void clickBrowse(){
        Actions act = new Actions(driver);
//        driver.findElement(By.xpath("//div[@id='uploadmode1']")).click();
        act.moveToElement(driver.findElement(By.xpath("//*[@id='file_wraper0']"))).click();

        //driver.findElement(By.xpath("//input[@id='uploadfile_0']")).sendKeys("/Users/Ajit/Desktop/320_500_football.jpg");
    }

    @AfterSuite
    public void close(){
//        driver.quit();
    }
}
