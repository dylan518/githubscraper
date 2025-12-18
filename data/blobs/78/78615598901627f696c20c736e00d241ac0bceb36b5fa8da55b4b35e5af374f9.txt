package tests;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeMethod;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;

public class CategoryList {
	WebDriver driver;

	@BeforeMethod
	public void beforeMethod() {
		System.setProperty("webdriver.chrome.driver",
				"C:\\Users\\SWHIZZ TECHNOLOGIES\\Downloads\\jars\\chromedriver.exe");

		driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.get("http://integratedtoolingsystems.in/1swishzz_staging/admin");
		driver.findElement(By.name("email")).sendKeys("admin@admin.com");
		driver.findElement(By.name("password")).sendKeys("123456");
		driver.findElement(By.name("submit")).click();
	}

	@Test(priority=1,groups="Category List")
	public void categoryListMenu() {
		driver.findElement(By.xpath("//span[contains(text(),'Categories List')]")).click();
		String expTitle = "Categories List";
		String actTitle = driver.findElement(By.xpath("//h3[contains(text(),'Categories List')]")).getText();
		System.out.println(actTitle);
		if (actTitle.equalsIgnoreCase(expTitle)) {
			System.out.println("Categories List Page displayed successfully");
			Assert.assertTrue(true);
		} else {
			Assert.assertTrue(false, "Categories List Page not displayed ");
		}

	}

	@Test(priority=2,groups="Category List")
	public void addCategory() {
		driver.findElement(By.xpath("//span[contains(text(),'Categories List')]")).click();
		driver.findElement(By.xpath("//header/div[1]/div[1]/div[1]/a[1]")).click();
		boolean addcatpage = driver.findElement(By.xpath("//h3[contains(text(),'Add Category')]")).isDisplayed();
		if (addcatpage) {
			System.out.println("Add Category Page displayed successfully");
			Assert.assertTrue(false);
		} else {
			Assert.assertTrue(false, "Add Category Page not displayed ");
		}

	}

	@Test(priority=3,groups="Courses List",dependsOnGroups="Category List" )
	public void addCategoryToList() {
		driver.findElement(By.xpath("//span[contains(text(),'Categories List')]")).click();
		driver.findElement(By.xpath("//header/div[1]/div[1]/div[1]/a[1]")).click();
		driver.findElement(By.xpath(
				"//body/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]"))
				.sendKeys("Offline Course");
		driver.findElement(By.xpath(
				"//body/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]"))
				.sendKeys("3");
		driver.findElement(By.xpath(
				"//body/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]"))
				.sendKeys("Meta data info");
		driver.findElement(By.xpath(
				"//body/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[4]/input[1]"))
				.sendKeys("meta description info");
		driver.findElement(By.xpath(
				"//body/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[5]/input[1]"))
				.sendKeys("meta keywords info");
		driver.findElement(By.xpath(
				"//body/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[6]/input[1]"))
				.click();
		boolean success = driver
				.findElement(By.xpath("//body/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]"))
				.isDisplayed();
		if (success) {
			System.out.println("Course created successfully");
			Assert.assertTrue(true);
		} else {
			Assert.assertTrue(false, "course not created ");
		}
	}

	@AfterMethod
	public void afterMethod() {
		driver.close();
	}

}
