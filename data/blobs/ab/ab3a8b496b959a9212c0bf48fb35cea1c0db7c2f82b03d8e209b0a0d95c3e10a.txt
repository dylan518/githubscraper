package project1comnopcommerce;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.edge.EdgeDriver;

import java.time.Duration;

public class Edge {
    public static void main(String[] args){
        String baseurl = "https://demo.nopcommerce.com/login?returnUrl=%2F%22";
        System.setProperty("webdriver.edge.driver", "drivers/msedgedriver.exe");
        WebDriver driver = new EdgeDriver();

        // Launch the URL
        driver.get(baseurl);

        //Maximise the window
        driver.manage().window().maximize();

        // We give implicit time to driver
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20));

        //Get the page of the Title
        String title = driver.getTitle();
        System.out.println("Page title is : " + title);

        // Get the current URL
        System.out.println("Current URL : "+ driver.getCurrentUrl());

        //; Get Page Source
        System.out.println("Page Source:" +driver.getPageSource());

        // Nevigate to Login Page by Clicking on login link
        driver.findElement(By.linkText(""));
        WebElement loginLink = driver.findElement(By.linkText("Log in"));
        loginLink.click();

        // Find the email field element
        WebElement emailField = driver.findElement(By.id("Email"));
        emailField.sendKeys("vimalpankhaniya@gmail.com");

        // Find the password field element
        WebElement passwordField = driver.findElement(By.name("Password"));
        passwordField.sendKeys("Lodnon3232");
        driver.quit();

    }}
