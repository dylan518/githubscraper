package com.selenium;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

public class MouseActions {

	public static void main(String[] args) {
		
		
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\ajith\\eclipse-workspace\\SELENIUM\\CHROME\\chromedriver.exe");
		
		
		WebDriver driver=new ChromeDriver();
		
		
		driver.get("http://www.leafground.com/pages/drop.html");
		
		driver.manage().window().maximize();
		
		Actions a = new Actions(driver);  // CREATING OBJECT TO ACCESS ACTIONS CLASS
		
		
		WebElement from_Element = driver.findElement(By.xpath("//div[@id='draggable']"));
		
		
		WebElement to_Element = driver.findElement(By.xpath("//div[@id='droppable']"));
		
		
		a.dragAndDrop(from_Element, to_Element).build().perform();   //DRAG AND DROP METHOD
		
		WebElement rightClick = driver.findElement(By.xpath("//div[@id='droppable']"));
		
		a.contextClick(rightClick).build().perform();   //FOR RIGHT CLICKING ANYTHING
		
		
		

	}

}
