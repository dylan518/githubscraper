package com.streak.Day6;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class ChildWindow {

	public static void main(String[] args) {
		
			WebDriver driver = new ChromeDriver();
			driver.get("https://www.wikipedia.org/");
			String parentWindowId = driver.getWindowHandle(); //parentWindow ID 
			driver.manage().window().maximize();
			// click on different web element to open new windows
			driver.findElement(By.xpath("//span[contains(text(),\"Apple\")]")).click();
			driver.findElement(By.xpath("//span[contains(text(),\"Google\")]")).click();
			driver.findElement(By.xpath("//span[contains(text(),\"with a donation.\")]")).click();

			// get all window handles
			Set<String> handles = driver.getWindowHandles();
			List<String> c = new ArrayList<String>(handles);
			//String[] windowHandles = handles.toArray(new String[0]);
			String thirdWindowHandle = c.get(3);
			driver.switchTo().window(thirdWindowHandle);
			System.out.println("end ");
			//driver.quit();

	}

}
