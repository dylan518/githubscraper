package com.internet.herokuapp.TestCases;

import com.internet.herokuapp.Configuration.BaseTest;
import com.internet.herokuapp.Pages.HorizontalSlider;
import com.internet.herokuapp.Pages.LandingPage;
import com.internet.herokuapp.Utilites.Data;
import org.testng.Assert;
import org.testng.annotations.Test;

public class HorizontalSliderTest extends BaseTest {

    @Test
    public void HorizontalSliderTest() {
        LandingPage lp = new LandingPage(driver);
        HorizontalSlider hs = new HorizontalSlider(driver);


        //URL Validation
        String baseUrl = driver.getCurrentUrl();
        System.out.println(baseUrl);
        Assert.assertEquals(baseUrl, Data.BASE_URL);
        System.out.println(Data.POSITIVE_MASSAGE);


        //HorizontalSlider button validation
        if (lp.getHorizontalSlider().isDisplayed())
        {
            String horizontalSlider = lp.getHorizontalSlider().getText();
            Assert.assertEquals("Horizontal Slider", horizontalSlider);
            System.out.println("HorizontalSlider button is visible and clickable");
            sleepTime(1000);
        }
        else {
            System.out.println(Data.NEGATIVE_ERROR_MASSAGE);
        }
        lp.getHorizontalSlider().click();


        //link Page URL Validation
        String HorizontalSliderLink = driver.getCurrentUrl();
        System.out.println("Given"+HorizontalSliderLink);
        Assert.assertEquals(HorizontalSliderLink, Data.BASE_URL+Data.HORIZONTAL_SLIDER_LINK);
        System.out.println("Link is validate");
        sleepTime(1000);


        //Header 1 Validation
        if (hs.getHorizontalSliderHeader().isDisplayed()) {
            String HorizontalSliderHeader = hs.getHorizontalSliderHeader().getText();
            Assert.assertTrue(true, HorizontalSliderHeader);
        } else {
            System.out.println(Data.NEGATIVE_ERROR_MASSAGE);
        }
        sleepTime(1000);

        //Sub_Header 2 Validation
        if (hs.getHorizontalSliderSubHeader2().isDisplayed()) {
            String HorizontalSliderSubHeader2 = hs.getHorizontalSliderSubHeader2().getText();
            Assert.assertTrue(true, HorizontalSliderSubHeader2);
        } else {
            System.out.println(Data.NEGATIVE_ERROR_MASSAGE);
        }
        sleepTime(1000);




    }
}
