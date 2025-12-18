package org.example;

import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.safari.SafariDriver;
import org.openqa.selenium.safari.SafariOptions;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;


public class BrowserManager extends Utils
{
    // Create Object For Load Properties Class
    LoadProp loadProp = new LoadProp();

    String sauceUrl = "https://oauth-nimeshsutharbs1109-f7b6c:c7c17b2e-8517-4108-bff1-cf57a746d9cb@ondemand.eu-central-1.saucelabs.com:443/wd/hub";
   // String browser =loadProp.getProperty("browser");
   // boolean cloud = false;

    boolean cloud = Boolean.parseBoolean(System.getProperty("cloud"));
    String browser = System.getProperty("browser");
    // Create Method To Open Browser
    public void openBrowser()
    {
        //Running In Cloud
        if (cloud)
        {
            System.out.println("Running In Cloud........");
            if(browser.equalsIgnoreCase("Chrome"))
            {
                //if Your Browser is Chrome In Properties
                ChromeOptions browserOptions = new ChromeOptions();
                browserOptions.setPlatformName("Windows 11");
                browserOptions.setBrowserVersion("latest");
                try
                {
                 driver = new RemoteWebDriver(new URL(sauceUrl), browserOptions);
                }
                catch (MalformedURLException e)
                {
                    throw new RuntimeException(e);
                }
            }
            else if (browser.equalsIgnoreCase("Safari"))
            {
                //if Your Browser is Safari In Properties
                SafariOptions browserOptions = new SafariOptions();
                browserOptions.setPlatformName("macOS 10.15");
                browserOptions.setBrowserVersion("15");
                try
                {
                    driver = new RemoteWebDriver(new URL(sauceUrl), browserOptions);
                }
                catch (MalformedURLException e)
                {
                    throw new RuntimeException(e);
                }
            } else if (browser.equalsIgnoreCase("Firefox"))
            {
                //if Your Browser is Safari In Properties
                FirefoxOptions browserOptions = new FirefoxOptions();
                browserOptions.setPlatformName("Windows 11");
                browserOptions.setBrowserVersion("latest-1");
                try
                {
                    driver = new RemoteWebDriver(new URL(sauceUrl), browserOptions);
                }
                catch (MalformedURLException e)
                {
                    throw new RuntimeException(e);
                }

            } else
            {
                //if Your Browser id Different From All If Condition
                System.out.println("Please Select Valid Browser");
            }
        }
        //Running In Local
        else
        {
            System.out.println("Running In Local........");
            if(browser.equalsIgnoreCase("Chrome"))
            {
                //if Your Browser is Chrome In Properties
                driver = new ChromeDriver();
            }
            else if (browser.equalsIgnoreCase("Safari"))
            {
                //if Your Browser is Safari In Properties
                driver = new SafariDriver();
            }
            else if (browser.equalsIgnoreCase("Firefox"))
            {
                //if Your Browser is Firefox In Properties
                driver = new FirefoxDriver();
            }
            else
            {
                //if Your Browser id Different From All If Condition
                System.out.println("Please Select Valid Browser");
            }
        }
        //Add Method For Maximize Window Of Browser
        driver.manage().window().maximize();
        //Give Waite Time For Load
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        //Add Url From Properties
        driver.get(loadProp.getProperty("Url"));
    }
    //Create Method To Close Browser
    public void closeBrowser()
    {
        driver.quit();
    }
}
