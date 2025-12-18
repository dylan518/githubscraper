package org.testclass;

import java.awt.AWTException;
import java.awt.event.KeyEvent;
import java.io.IOException;
import java.time.Duration;
import java.util.Set;

import org.base.BaseClass;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;
import org.pom.LoginPagePom;

public class TestingClassEdge extends BaseClass {

	public static BaseClass b = new BaseClass();
	public static LoginPagePom pom;

	@BeforeClass
	public static void getBrowser() {
		try {
			b.getDriver("Edge");
			b.windowsMax();
			System.out.println("Browser Launched Successfully");
			//			Report - Browser Launched Successfully			
		} catch (Exception e) {
			System.out.println("Browser Not Launched Successfully");
			//			Report - Browser Not Launched Successfully - Failure - Screenshot			
		}		

	}
	@Before
	public void urlLanunched() {
		try{
			b.getUrl("https://www.saucedemo.com/");
			driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(20));
			System.out.println("URL Launched Successfully");
			//			Report - Url Launched Successfully			
		} catch (Exception e) {
			System.out.println("URL Not Launched Successfully");
			//			Report - Url Not Launched Successfully - Failure - Screenshot	
		}

	}

	@Test
	public void loginDataEntering() {
		try {

			pom = new LoginPagePom();

			WebElement userName = pom.getUserName();
			userName.sendKeys("standard_user");
			//			userName.sendKeys(b.excelRead(0, 0));
			WebElement passWord = pom.getPassWord();
			passWord.sendKeys("secret_sauce");
			//			passWord.sendKeys(b.excelRead(0, 1));

			b.getThread(5000);
			b.screenShot("1.Login");

			WebElement login = pom.getLogin();
			b.buttonClick(login);

			WebElement openMenu = pom.getOpenMenu();
			b.buttonClick(openMenu);

			b.getThread(3000);

			WebElement allItems = pom.getAllItems();
			b.buttonClick(allItems);

			b.getThread(3000);

			WebElement closeMenu = pom.getCloseMenu();
			b.buttonClick(closeMenu);

			b.getThread(3000);

			WebElement productSort = pom.getProductSort();
			b.buttonClick(productSort);
			b.getSelect(productSort, "value", "hilo");

			b.getThread(3000);

			WebElement fleeceJacket = pom.getFleeceJacket();
			b.buttonClick(fleeceJacket);

			b.getThread(3000);

			WebElement backPack = pom.getBackPack();
			b.buttonClick(backPack);

			b.getThread(3000);

			WebElement tshirt = pom.getTshirt();
			b.buttonClick(tshirt);

			b.getThread(3000);

			WebElement redTshirt = pom.getRedTshirt();
			b.buttonClick(redTshirt);

			b.getThread(3000);

			WebElement bikeLight = pom.getBikeLight();
			b.buttonClick(bikeLight);

			b.getThread(3000);

			WebElement oneSie = pom.getOneSie();
			b.buttonClick(oneSie);

			b.getThread(3000);

			WebElement shopCartLink = pom.getShopCartLink();
			b.buttonClick(shopCartLink);

			b.getThread(3000);

			b.getThread(5000);
			b.screenShot("2.Your_Cart");

			WebElement removeTshirt = pom.getRemoveTshirt();
			b.buttonClick(removeTshirt);

			b.getThread(3000);

			WebElement removeOneSie = pom.getRemoveOneSie();
			b.buttonClick(removeOneSie);

			b.getThread(3000);

			WebElement removeBikeLight = pom.getRemoveBikeLight();
			b.buttonClick(removeBikeLight);

			b.getThread(3000);
			b.screenShot("3.Check_Out");

			WebElement checkout = pom.getCheckout();
			b.buttonClick(checkout);	


			System.out.println("CheckOut Successfully");
			//			Report - CheckOut Successfully			
		} catch (Exception e) {
			System.out.println("CheckOut not Successfully");
			//			Report - CheckOut not Successfully - Failure - Screenshot
		}
	}

	@After
	public void clicklogin() {
		try {

			pom = new LoginPagePom();

			WebElement firstName = pom.getFirstName();
			b.buttonClick(firstName);
			b.gettextSend(firstName, "Abarna");

			b.getThread(3000);

			WebElement lastName = pom.getLastName();
			b.buttonClick(lastName);
			b.gettextSend(lastName, "R");

			b.getThread(3000);

			WebElement postalCode = pom.getPostalCode();
			b.buttonClick(postalCode);
			b.gettextSend(postalCode, "600042");

			b.getThread(5000);
			b.screenShot("4.Proceed");

			WebElement proceed = pom.getProceed();
			b.buttonClick(proceed);

			WebElement text = pom.getScrollText();
			b.getScroll("true", text);

			b.getThread(5000);
			b.screenShot("5.Finish");

			WebElement finish = pom.getFinish();
			b.buttonClick(finish);						

			System.out.println("Finish Clicked Successfully");
			//			Report - Finish Clicked Successfully	
		} catch (Exception e) {
			System.out.println("Reserve not Clicked Successfully");
			//			Report - Finish not Clicked Successfully - Failure - Screenshot
		}
	}

	@AfterClass
	public static void nextPage() {
		try {

			pom = new LoginPagePom();

			b.getThread(5000);			
			b.screenShot("6.Thank You for Your Order");

			WebElement backHome = pom.getBackHome();
			b.buttonClick(backHome);	

			WebElement openOutMenu = pom.getOpenOutMenu();
			b.buttonClick(openOutMenu);

			b.getThread(3000);

			WebElement out = pom.getOut();
			b.buttonClick(out);

			b.getThread(5000);
			b.screenShot("7.Home_Page");			

			System.out.println("Logout Successfully");
			//			Report - Logout Successfully	
		} catch (Exception e) {
			System.out.println("Logout not Successfully");
			//			Report - Logout not Successfully - Failure - Screenshot
		}
	}
}
