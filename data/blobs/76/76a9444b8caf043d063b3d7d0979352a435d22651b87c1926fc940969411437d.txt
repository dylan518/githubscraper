package com.obsqura.testprogram;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class TestProgram {

	public WebDriver driver;
	
	@BeforeTest
	public void Browser() {
		driver = new ChromeDriver();
		driver.get("https://www.selenium.obsqurazone.com/simple-form-demo.php");
		driver.manage().window().maximize();
		Assert.assertEquals(false, driver.findElement(By.xpath("(//div[@class='card-header'])[2]")).isDisplayed());		
	}
	
	@Test
	public void simpleFormDemo() throws InterruptedException {
		driver.findElement(By.id("single-input-field")).click();
		driver.findElement(By.className("form-control")).sendKeys("Obsqura");
		Thread.sleep(2000);
		driver.findElement(By.cssSelector("button[id='button-one']")).click();
		Thread.sleep(2000);
	}
	
	@AfterTest
	public void Browserclose() {
		driver.close();
	}
}

