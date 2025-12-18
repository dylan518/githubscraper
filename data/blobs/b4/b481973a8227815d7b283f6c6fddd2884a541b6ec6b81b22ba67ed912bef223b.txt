package selenium;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
public class GetMethod {
	public static void main(String[] args) throws Exception {	
		WebDriver c = new FirefoxDriver();
		Thread.sleep(2000);
    	c.get("https://www.flipkart.com/");	
    	
		String acttitle = c.getTitle();
		String exptitle = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!";
		System.out.println(acttitle);
		
		if (acttitle.equals(exptitle)) {
			System.out.println("Title has been match");
		} else {
			System.out.println("Title has not been match");
		}	
		String acturl = c.getCurrentUrl();
		String expurl = "https://www.flipkart.com/";
		System.out.println(acturl);
		
		String page = c.getPageSource();
		System.out.println(page);	
		
	}
}