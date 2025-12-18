package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import pages.CategoriesAndToolsPage;
import pages.CheckOutPage;
import pages.RegisterPage;

public class CheckOutTest extends BaseTest{

    @Test
    public void checkOut() throws InterruptedException {
        RegisterPage registerPage=new RegisterPage(driver);
        registerPage.registerPage();

        CategoriesAndToolsPage categoriesAndToolsPage=new CategoriesAndToolsPage(driver);
        categoriesAndToolsPage.selectTools();

        Assert.assertEquals(driver.getCurrentUrl(),"https://practicesoftwaretesting.com/#/category/hand-tools","URL se ne podudaraju.");

        categoriesAndToolsPage.addHammerIntoCart();
        categoriesAndToolsPage.addSheetSanderIntoCart();
        Thread.sleep(1000);

        CheckOutPage checkOutPage=new CheckOutPage(driver);
        checkOutPage.clickOnCartButton();
        Thread.sleep(1000);
        System.out.println(checkOutPage.getFirstAmount());
        System.out.println(checkOutPage.getSecondAmount());
        System.out.println(checkOutPage.getTotalAmount());
        System.out.println(checkOutPage.totalSum());

        Assert.assertEquals(checkOutPage.totalSum(),checkOutPage.getTotalAmount(), "Sume se ne poklapaju. ");

    }

}
