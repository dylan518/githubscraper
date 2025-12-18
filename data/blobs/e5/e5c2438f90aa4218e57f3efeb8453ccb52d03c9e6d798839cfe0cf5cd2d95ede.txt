package org.qa23.automationQA.actionHome;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

import java.util.Objects;

public class ActionsHome {
    public static void main(String[] args) throws InterruptedException {

        WebDriverManager.chromedriver().setup();
        WebDriver webDriver = new ChromeDriver();
        webDriver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html");
        webDriver.manage().window().maximize();
        Actions actions = new Actions(webDriver);
        actions.contextClick(webDriver.findElement(By.cssSelector(".context-menu-one"))).perform();
        Thread.sleep(1000);
        actions.click(webDriver.findElement(By.cssSelector(".context-menu-list > li:last-child"))).perform();
        Alert alert = webDriver.switchTo().alert();
        if (Objects.nonNull(alert) && alert.getText() != null) {
            if (alert.getText().equals("alert: clicked: quit")) {
                System.out.println("Test COMPLETED: text equal");
            } else {
                System.out.println("Test COMPLETED: text notEqual");
                System.out.println("Actual res: [" + alert.getText()+"]");
                System.out.println("Expected res: [alert: clicked: quit]");
            }
            alert.accept();
        }
        webDriver.quit();
    }
}
