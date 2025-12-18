package com.udemy.lambda.functional_interfaces.supplier;


import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.edge.EdgeDriver;

import java.util.Map;
import java.util.function.Supplier;

public class DriverFactory {

    private static final Supplier<WebDriver> chromeSupplier = () -> {
        System.setProperty("webdriver.chrome.driver", "src/main/resources/drivers/chromedriver.exe");
        return new ChromeDriver();
    };

    private static final Supplier<WebDriver> edgeSupplier = () -> {
        System.setProperty("webdriver.edge.driver", "src/main/resources/drivers/msedgedriver.exe");
        return new EdgeDriver();
    };

    private static final Map<String, Supplier<WebDriver>> MAP = Map.of(
            "chrome", chromeSupplier,
            "edge", edgeSupplier
    );
    
    public static WebDriver getDriver(String browser) {
        return MAP.get(browser).get();
    }
}
