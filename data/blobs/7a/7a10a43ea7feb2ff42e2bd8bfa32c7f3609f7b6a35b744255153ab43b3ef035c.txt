package stepDefinitions;

import org.openqa.selenium.WebDriver;
import org.testng.Assert;

import factory.BaseClass;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import pageObjects.LeadGeneration;

public class LeadGenerationStepDefinitions {
	WebDriver driver;
	LeadGeneration leadgeneration;

	public LeadGenerationStepDefinitions() {
		driver = BaseClass.getDriver();
		leadgeneration = new LeadGeneration(driver);
	}

	@Then("the title {string} should be shown to the user")
	public void the_title_should_be_shown_to_the_user(String Hometext) {
		Assert.assertTrue(leadgeneration.validateHomeText());
	}

	@Then("the user clicks on the {string} option")
	public void the_user_clicks_on_the_option(String CRM) {
		leadgeneration.userClickOnTheCRMOption();
	}

	@When("the user clicks on the {string} option under the Sales Pipeline")
	public void the_user_clicks_on_the_option_under_the_sales_pipeline(String string) {
		leadgeneration.userClickOnTheLeadOption();
	}

	@Then("the lead page should be displayed")
	public void the_lead_page_should_be_displayed() {
		Assert.assertTrue(leadgeneration.validateLeadText());
	}

	@Then("the following text should be visible to the user {string}")
	public void the_following_text_should_be_visible_to_the_user(String headerListValidate) {
		Assert.assertTrue(leadgeneration.validateHeaderList(headerListValidate));
	}

//	}
//
//	@Then("in the lead page when the territory in the {string} option")
//	public void in_the_lead_page_when_the_territory_in_the_option(String string) {
//	    // Write code here that turns the phrase above into concrete actions
//	    throw new io.cucumber.java.PendingException();
//	}
//
//	@Then("according to the territory the lead should be shown")
//	public void according_to_the_territory_the_lead_should_be_shown() {
//	    // Write code here that turns the phrase above into concrete actions
//	    throw new io.cucumber.java.PendingException();
//	}

}
