package test.US02_US13_US16_US33_US35_US49.US_49;

import org.openqa.selenium.Keys;
import org.testng.annotations.Test;
import pages.AdminDashboard;
import utilities.ConfigReader;
import utilities.Driver;
import utilities.ReusableMethods;

public class US49_TC04 {

    //Kayıtlı States sayısının görüntülenebilmelidir

    @Test
    public void test04() {
        AdminDashboard adminDashboard = new AdminDashboard();

        //Kullanici Hause Heaven Admin sayfasina gider
        Driver.getDriver().get(ConfigReader.getProperty("urlAdmin"));

        adminDashboard.adminEMail.sendKeys("admin21" + Keys.TAB);
        adminDashboard.adminPassword.sendKeys("951847" + Keys.TAB);
        adminDashboard.adminRemember.click();
        adminDashboard.adminSignIn.click();
        adminDashboard.adminGirisKontrol.isDisplayed();

        adminDashboard.locations.click();
        adminDashboard.locationsBasligindakiler.isEnabled();


        adminDashboard.states.click();
        adminDashboard.stetasSayisi.isDisplayed();
        ReusableMethods.waitFor(3);
        adminDashboard.stetasSayisi.isEnabled();
        Driver.closeDriver();
    }
}
