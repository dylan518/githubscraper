package com.qa.pages;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import com.qa.base.FrameWorkBase1;

public class TakeScreenShotPage extends FrameWorkBase1 {

	@FindBy(xpath = "//input[@id='email']")
	WebElement login;

	@FindBy(xpath = "//input[@title='Password']")
	WebElement pass;

	@FindBy(xpath = "//button[@id='send2']")
	WebElement loginclick;

	public TakeScreenShotPage() {
		PageFactory.initElements(driver, this);
	}

	public void takeScreenShotMethod() {

		String user1 = prop.getProperty("username1");
		login.sendKeys(user1);

		String pass1 = prop.getProperty("password1");
		pass.sendKeys(pass1);

//		String titText = driver.getTitle();

		loginclick.click();

		String titText = driver.getTitle();

		if (titText.equalsIgnoreCase("Customer Login")) {

			TakesScreenshot src = (TakesScreenshot) driver;

			File srcFile = src.getScreenshotAs(OutputType.FILE);

			File desSrcPath = new File("C:\\Users\\pchan\\eclipse-workspace\\Guru99\\ScreenShot\\Image33.jpeg");

//			File desSrcPath = new File(path + "ScreenShot\\\\Image1.png");

			try {
				FileUtils.copyFile(srcFile, desSrcPath);
			} catch (IOException e) {

			}

		}

		else {
			System.out.println("login su");

		}

	}

}
