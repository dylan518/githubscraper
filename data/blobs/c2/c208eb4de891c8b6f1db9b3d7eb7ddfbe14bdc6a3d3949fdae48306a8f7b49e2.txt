package vm;

import org.testng.Assert;
import org.testng.annotations.Test;

public class AppTest {

	@Test
	public void InValidCredentialsTest() {
		App myApp = new App();
		Assert.assertEquals(0, myApp.userLogin("abc", "password"));
	}

	@Test
	public void ValidCredentialsTest() {
		App myApp = new App();
		Assert.assertEquals(1, myApp.userLogin("abc", "password"));
	}
}
