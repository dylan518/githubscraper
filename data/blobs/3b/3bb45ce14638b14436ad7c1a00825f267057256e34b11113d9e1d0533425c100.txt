package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import utilities.WaitUtility;

public class ManageNewsPage {

	public WebDriver driver;
	public ManageNewsPage(WebDriver driver)
	{
		this.driver=driver;
		PageFactory.initElements(driver,this);
	}
	
	
	@FindBy(xpath="//i[@class='fas fa-arrow-circle-right']//parent::a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']")private WebElement manageNewsInfo;
	@FindBy(linkText ="Manage News")private WebElement manageNewsPage;
	@FindBy(xpath="//i[@class='fas fa-edit']//parent::a[@class='btn btn-rounded btn-danger']")private WebElement newButton;
	@FindBy(xpath="//textarea[@placeholder='Enter the news']")private WebElement newsTextField;
	@FindBy(xpath="//button[@type='submit']")private WebElement saveButton;
	@FindBy(xpath="//div[@class='alert alert-success alert-dismissible']")private WebElement messageSuccess;
	@FindBy(xpath="//i[@class='fas fa-edit']//parent::a[@href='https://groceryapp.uniqassosiates.com/admin/news/edit?edit=1576&page_ad=1']")private WebElement editButtonClick;
	@FindBy(xpath="//textarea[@id='news']")private WebElement editNewsTextField;
	@FindBy(xpath="//button[@name='update']")private WebElement updateButtonClick;
	@FindBy(xpath="//div[@class='alert alert-success alert-dismissible']")private WebElement editMessageSuccess;
	
	
	
	
	public ManageNewsPage clickOnmanageNewsInfo()
	{
	    manageNewsInfo.click();
	    return this;
    }
	
	public boolean verifyManageNewsPageNavigated()
	{
		boolean isManageNewsPageNavigated=manageNewsPage.isDisplayed();
		return isManageNewsPageNavigated;
	}
	public ManageNewsPage clickOnNewButton() 
	{
		newButton.click();
		return this;
	}
	public ManageNewsPage enteringNewsOnTextField(String news) 
	{
		newsTextField.sendKeys(news);
		return this;
       
    }
	public ManageNewsPage clickOnSaveButton()
	{
		saveButton.click();
		return this;
	}
	public boolean verifyAddedNews()
	{
		boolean isMessageSuccessVerified=messageSuccess.isDisplayed();
		return isMessageSuccessVerified;
	}
	public ManageNewsPage clickOnEditButton()
	{
		editButtonClick.click();
		return this;
	}
	public ManageNewsPage editNewsOnNewsTextField(String updatedNews)
	{
		editNewsTextField.clear();
		editNewsTextField.sendKeys(updatedNews);
		return this;
	}
	
	public ManageNewsPage clickOnUpdateButton()
	{
		updateButtonClick.click();
		return this;
	}
	public ManageNewsPage updateButtonclickableWait()
	{
		WaitUtility waitutility=new WaitUtility();
		waitutility.elementToBeSelectedFluentWait(driver,updateButtonClick);
		return this;
	}
	public boolean verifyUpdatedNews() {
        boolean isMessageUpdatedSuccessfully=editMessageSuccess.isDisplayed();
        return isMessageUpdatedSuccessfully;
    }
}