package id.ac.ui.cs.advprog.eshop;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class EshopApplicationTests {

	@Test
	void testRunApp() {
		// Exercise
		EshopApplication application = new EshopApplication();
		String[] args = { "test" };
		EshopApplication.main(args);

		// Verify
		assertEquals("test", args[0]);

	}

}
