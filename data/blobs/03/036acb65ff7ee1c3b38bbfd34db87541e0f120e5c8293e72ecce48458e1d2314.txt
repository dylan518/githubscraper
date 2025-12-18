package herokuapp;

import common.TestBase;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import pages.NestFramesPage;
import supports.Browser;

public class NestFramesTest extends TestBase {
    NestFramesPage nestFramesPage;

    @BeforeClass
    void openBrowser(){
        Browser.launchBrowser("chrome");
    }

    @BeforeMethod
    void open(){
        nestFramesPage = new NestFramesPage();
        nestFramesPage.open();
    }

    @Test
    void verifyFrameContent(){
        Assert.assertEquals(nestFramesPage.checkDisplayOfTextLeft(),"LEFT");
        Assert.assertEquals(nestFramesPage.checkDisplayOfTextMiddle(),"MIDDLE");
        Assert.assertEquals(nestFramesPage.checkDisplayOfTextRight(),"RIGHT");
        Assert.assertEquals(nestFramesPage.checkDisplayOfTextRBottom(),"BOTTOM");
    }

    @AfterClass
    void tearDown(){
        Browser.quit();
    }
}
