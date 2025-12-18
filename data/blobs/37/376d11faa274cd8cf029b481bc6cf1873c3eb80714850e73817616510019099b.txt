package org.stepdefinition;

import org.lib.BaseClass;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

import io.cucumber.core.api.Scenario;
import io.cucumber.java.After;
import io.cucumber.java.Before;

public class Hooks extends BaseClass {
	@Before(order = 1)
	public void bf() {
		browserLaunch();

	}
	@Before(order = 3)
	public void bf1() {
		System.out.println("before launch take a screenshot");

	}
	@Before(order = 2)
	public void bf2() {
		maxWin();
	}

	@After(order = 1)
	public void Af() {
		browserClose();

	}
	@After(order = 8)
	public void Af1(Scenario s) {
		System.out.println("after launch take a screenshot");
		
		if (s.isFailed()) {
			
			TakesScreenshot ts= (TakesScreenshot)s;
			byte[] ss = ts.getScreenshotAs(OutputType.BYTES);
			s.embed(ss, "image/png");
			System.out.println("getscreentshot:"+s.getName());
			
		}
		
		

	}

}
