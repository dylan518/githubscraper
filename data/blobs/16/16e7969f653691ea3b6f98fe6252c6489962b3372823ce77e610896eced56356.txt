import org.openqa.selenium.support.PageFactory;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class FooterTest extends  Base {

    FooterSection footer;
    @BeforeMethod

    void openBrowser() {
        setUp("https://www.amazon.com");
        driver.manage().window().maximize();
        footer = PageFactory.initElements(driver, FooterSection.class);
    }
    @Test
    void checkFooterVisibility() {
        boolean footerVisible = footer.isFooterareaVisible();
        Assert.assertTrue(footerVisible);
    }

    @Test
    void checkSubFooterVisibility() {
        boolean subFootervisible = footer.isSubFooterareaVisible();
        Assert.assertTrue(subFootervisible);
    }

    @Test
    void checkFooterTitlesPresence() {
        boolean fTitletest = footer.arefooterLinksPresent();
        Assert.assertTrue(fTitletest);
    }
    @Test
    void checkFooterTitles() {
        int mainTitleCount = footer.getfooterTitleCount();
        Assert.assertTrue(mainTitleCount ==32);

    }
    @Test
    void checkTotalFooterTitles() {
        int actualCount = footer.getTotalFooterTitle();
        int expectedCount = 78;
        Assert.assertEquals(actualCount, expectedCount);
    }
    @AfterMethod
    void cleanUp(){
         clean();
    }

}

