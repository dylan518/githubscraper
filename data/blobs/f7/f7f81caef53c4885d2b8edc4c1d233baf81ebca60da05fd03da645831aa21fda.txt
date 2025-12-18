package Page;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class AddUser {

    WebDriver driver;

    @FindBy(xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'][1]")
    WebElement UserRoleList;
    @FindBy(xpath = "//div[@class = 'oxd-select-option'][3]")
    WebElement UserRole;
    @FindBy(xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i")
    WebElement UserStatusList;
    @FindBy(xpath = "//div[@class='oxd-select-dropdown --positon-bottom']/div[@class = 'oxd-select-option'][2]")
    WebElement UserStatus;
    @FindBy(xpath = "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']")
    WebElement EmployeeName;
    @FindBy(xpath = "(//*[contains(text(),Username)]/../following-sibling::*)[1]/input")
    WebElement Username;
    @FindBy(xpath = "(//*[contains(text(),'Password')]/../following-sibling::*)[1]/input")
    WebElement Password;
    @FindBy(xpath = "(//*[contains(text(),'Confirm')]/../following-sibling::*)[1]/input")
    WebElement ConfirmPassword;
    @FindBy(xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'")
    WebElement SaveButton;

    public AddUser(WebDriver driver){
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }
    public void openUserRoleList(){
        UserRoleList.click();
    }
    public void selectUserRole(){
        UserRole.click();
    }
    public void openUserStatusList(){
        UserStatusList.click();
    }
    public void selectUserStatus(){
        UserStatus.click();
    }
    public void saisir_EmployeeName(String employeename){
        EmployeeName.sendKeys(employeename);
    }
    public void saisir_Username(String username){
        Username.sendKeys(username);
    }
    public void saisir_Password(String password){
        Password.sendKeys(password);
    }
    public void saisir_ConfirmPassword(String confirmpassword){
        ConfirmPassword.sendKeys(confirmpassword);
    }
    public void SaveButton(){
        SaveButton.click();
    }
    public void modifUserName(){
        Username.clear();
        UserRole.sendKeys("PEPE");
    }

}



