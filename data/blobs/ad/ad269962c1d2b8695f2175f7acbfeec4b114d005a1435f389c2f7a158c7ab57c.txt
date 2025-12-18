package StepDefinitions;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class TestcaseSteps {
	WebDriver driver;

	@Given("I am on espncricinfo Application")
	public void i_am_on_espncricinfo_application() {
		String path=System.getProperty("user.dir");
		System.setProperty("webdriver.chrome.driver",path+"\\lib\\chromedriver_127.exe");
		driver = new ChromeDriver();	
		driver.get("https://www.espncricinfo.com/");
	}

	@When("I mousehover on Live scores and click on LiveScoresHome")
	public void i_mousehover_on_live_scores_and_click_on_live_scores_home() {
		driver.findElement(By.xpath("//*[text()='Live Scores']")).click();
	}

	@Then("I am able to see Live Cricket Matches text with the Result")
	public void i_am_able_to_see_live_cricket_matches_text_with_the_result() {

		String expectedString =driver.findElement(By.xpath("//*[text()='Live Cricket Matches']")).getText();
		Assert.assertEquals("Live Cricket Matches", expectedString);

	}

	


}
