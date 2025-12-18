package airplainApplication;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.testng.Assert;

public class Coupon_Apply {
	@FindBy(xpath="(//div[@class='flexCol padL10 width100'])[2]")
	WebElement select_coupon;
	
	@FindBy(xpath="//div[text()='Awesome! Promo discount applied']")
	WebElement validate_discount;
	
	@FindBy(xpath="//span[text()='VIEW ALL COUPONS']")
	WebElement view_all_coupon;
	
	
	public void select_coupon()
	{
		select_coupon.click();
	}
	public void validate_discount()
	{
		//Assert.assertEquals(validate_discount.isDisplayed(),true, "coupon is not applied");
	Assert.assertEquals(validate_discount.getText(),"Awesome! Promo discount applied" ,"Promo code not applied");
		}
	public void view_all_coupon()
	{
		view_all_coupon.click();
	}
	
	public Coupon_Apply(WebDriver driver)
	{
		PageFactory.initElements(driver,this);
	}

}
