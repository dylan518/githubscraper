package SeleniumSessions;

import java.time.Duration;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class ImplicityWait {

	public static void main(String[] args) {
		
		WebDriver driver = new ChromeDriver();
		
	//	driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);  //sel 3.x//depricated implicitywait 
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));  //sel 4.x
	
	   //implicityWait is global wait: 10 secs
	    //global wait will be appliced for all the element by default
	    //FE  -- imp wait will be applied automatically to all FE
	    
	    
	    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/login");
	    
	  //driver.findElement(By.id("input-email111")).sendKeys("meena123@gmail.com"); //NoSuchElementException  when pass wrong locater
	    driver.findElement(By.id("input-email")).sendKeys("meena123@gmail.com");  //10-5=5  -- 5 sec ignored
	    driver.findElement(By.id("input-password")).sendKeys("meena123");   //10-2=8  -- 8 secs ignored
	    driver.findElement(By.xpath("//input[@value='Login']")).click();   //10-6=4
	    //e4 ele --10
	    //e5 ele --10
	    //e6 ele --10
	    
	    //home page: 20 secs
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20));
	    //global wait : 20 secs
	    //e7 -20 secs
	    //e8 - 20 secs
	    //e9 - 20 secs
	    
	    //login page: 20 secs ---> 10secs
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
	    
	    
	    //register: 10 secs --> 5 secs:
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));
	    
	    //login: 5 secs--> 10 secs
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
	    
	    //forgotpwd : 0 secs  -- nullify of imp wait
	    driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(0));
	    
	    //latest value of implicitly wait always will be applied.
	    
	    //if you want to go to login page again,current imp wait is 0 . we have to write imp wait again to 10
	    
	    // this is the big disadvantage of imp wait .
	    //1.we have to change the imp wait to each page according to how much wait ele needed.
	    //2.also imp wait applied for all the eles on the page.it impact the performance of application.
	    //so never use imp wait in frame work at all.
	    //3. imp wait only for web element : svg, iframe, webelement
	    //imp wait not applicable for shadow dom. shadow dom we use java script not driver.findElement
	    //4. imp wait doesn't support non web element : title, url, alerts-js
	}

}



