package com.evy.selenium;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebElement;

import java.io.File;
import java.io.IOException;

/**
 * How to capture screenshots
 */
public class Session22 {
    public static void main(String[] args) throws IOException {
        Driver.getDriver().get("https://demo.nopcommerce.com/");
        //Take full page screenshot
        TakesScreenshot ts=(TakesScreenshot) Driver.getDriver();
        File src=ts.getScreenshotAs(OutputType.FILE);
        File trg=new File("screenshot/homepage.png");
        FileUtils.copyFile(src,trg);

        //Take section screenshot
        WebElement section=Driver.getDriver().findElement(By.cssSelector(".top-menu.notmobile"));
        File src1=section.getScreenshotAs(OutputType.FILE);
        File trg1=new File("screenshot/section.png");
        FileUtils.copyFile(src1,trg1);

        //screenshot of element
        WebElement search_box=Driver.getDriver().findElement(By.id("small-searchterms"));
        File src2=search_box.getScreenshotAs(OutputType.FILE);
        File trg2=new File("screenshot/search_box.png");
        FileUtils.copyFile(src2,trg2);

        Driver.quitDriver();
    }
}
