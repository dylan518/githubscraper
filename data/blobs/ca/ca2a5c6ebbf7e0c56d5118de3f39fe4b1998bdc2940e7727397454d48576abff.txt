package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class HomePage extends BasePage{
    //Tab elements
    private final By rezervationElement =By.xpath("//a[normalize-space()='Rezervasyon']");
    private final By campaignsElement = By.xpath("//a[normalize-space()='Kampanyalar']");
    private final By officeElement = By.xpath("//a[normalize-space()='Ofisler']");
    private final By fleetElement = By.xpath("//a[normalize-space()='Filo']");
    private final By informationElement = By.xpath("//a[normalize-space()='Bilgilendirme']");
    private final By investorRelationElement = By.xpath("//a[contains(text(),'Yatırımcı İlişkileri')]");

    public HomePage(WebDriver driver) {
        super(driver);
    }

    public void clickRezervation() {
        clickElement(rezervationElement);
    }

    public void clickCampaigns() {
        clickElement(campaignsElement);
    }

    public void clickOffices() {
        clickElement(officeElement);
    }

    public void clickFleet() {
        clickElement(fleetElement);
    }

    public void clickInformation(){
        clickElement(informationElement);
    }

    public void clickInvestorRelations(){
        clickElement(investorRelationElement);
    }

}
