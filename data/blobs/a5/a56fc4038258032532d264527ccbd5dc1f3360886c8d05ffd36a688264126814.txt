package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.testng.Assert;
import testData.BaseData;
import util.PageHelper;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NotesPage
{
    private AddressbookPage addressbookPage;
    private WebDriver driver;
    public NotesPage (WebDriver driver) {
       // super(driver);
        this.driver = driver;
        this.addressbookPage = new AddressbookPage(driver);
        PageFactory.initElements(driver, this);
    }

    @FindBy(xpath="//button[.='New Note']")
    private WebElement newNoteButton;
    @FindBy(xpath="//textarea[@data-placeholder='Add new notes content here...']")
    private WebElement notesArea;
    @FindBy(xpath="//span[.='Create Note']")
    private WebElement createNoteLabel;
    @FindBy(xpath="//h2[.='Update Note']")
    private WebElement  updateNoteLabel;
    @FindBy(id="tid-add-notes")
    private WebElement addNotesButton;

    @FindBy(id="tid-update-notes")
    private WebElement updateNotesButton;
    @FindBy(xpath="(//mat-icon[@svgicon='inv-ellipsis-h'])")
    private WebElement clickFirstNotes;


    @FindBy(xpath="//button[contains(text(),'Edit')]")
    private WebElement editButtonForFirstNotes;

    @FindBy(xpath="//button[@id='tid-update-notes']")
    private WebElement updateButtonForNotes;

    @FindBy(xpath="//button[contains(text(),'Delete')]")
    private WebElement deleteButtonForNotes;
    @FindBy(xpath = "//notifier-notification[contains(@class,'notifier__notification') and .= 'Note created successfully']")
    private WebElement notesCreationMessage;

    @FindBy(xpath = "//notifier-notification[contains(@class,'notifier__notification') and .= 'Note updated successfully']")
    private WebElement notesUpdateMessage;


    @FindBy(xpath = "//notifier-notification[contains(@class,'notifier__notification') and .= 'Note deleted successfully']")
    private WebElement notesDeleteMessage;

    @FindBy(xpath = "//notifier-notification[contains(@class,'notifier__notification') and contains(., 'File format is not supported.')]")
    private WebElement invalidFileAlertMessage;
    @FindBy(xpath ="//input[@type='file']")
    private WebElement uploadAttachment;

    @FindBy(xpath = "//ngx-spinner//div[contains(@class,'la-ball-fussion')]")
    private WebElement loader;

    @FindBy(xpath = "//app-msg-dialog//button[.='Delete']")
    private WebElement deleteButtonInPopUp;
    @FindBy( id="tid-dialog-close-icon")
    private WebElement closeButtonInForm;

    @FindBy(xpath="//span[contains(text(),'Notes')]")
    private WebElement notesMenu;

    @FindBy(tagName="app-create-edit-note")
    private WebElement notesForm;

    public <T extends BaseData> boolean addNotes(T obj, HashMap<String, String>[] notesTestData)
    {
        boolean isNotesCreated = false;
        try {
            obj.generateDataForCreateNotes();
            for (int i = 0; i < notesTestData.length; i++)
            {
                PageHelper.invisibilityOfElement(driver,loader);
                PageHelper.javascriptClick(driver, notesMenu);
                System.out.println("Am I clicking 1");
                PageHelper.javascriptClick(driver, newNoteButton);
                PageHelper.invisibilityOfElement(driver, loader);
                System.out.println("Am I clicking 2");
                PageHelper.sendKeysToElement(driver, notesArea, notesTestData[i].get("Notes"));
                if(notesTestData[i].containsKey("Attachment")) {
                    File f = new File(notesTestData[i].get("Attachment"));
                    System.out.println("File path is " + f.getAbsolutePath());
                    //PageHelper.javascriptClick(driver,attachFile);
                    PageHelper.uploadFile(driver, uploadAttachment, f.getAbsolutePath());
                    PageHelper.invisibilityOfElement(driver, loader);
                }
                PageHelper.javascriptClick(driver, addNotesButton);
                if(isNotesSuccessfullyCreated())
                {
                    isNotesCreated =true;
                }
                else {
                    isNotesCreated=false;
                    break;
                }

            }
        }
        catch (Exception e)
        {
            Assert.fail(String.valueOf(e));
            return isNotesCreated;
        }

        return  isNotesCreated;
    }

    public void deleteNotes(WebDriver driver) {
        try {
            PageHelper.invisibilityOfElement(driver, loader);
            PageHelper.javascriptClick(driver, notesMenu);
            PageHelper.javascriptClick(driver, clickFirstNotes);
            PageHelper.javascriptClick(driver, deleteButtonForNotes);
            PageHelper.javascriptClick(driver, deleteButtonInPopUp);
            PageHelper.invisibilityOfElement(driver, loader);
        }
        catch(Exception e)
        {
             Assert.fail(String.valueOf(e));
        }
    }

    public boolean validateDeleteNotes()
    {
        deleteNotes(driver);
        return  isNotesSuccessfullyDeleted();
    }

    public <T extends BaseData> boolean editNotes(T obj, HashMap<String, String>[] notesTestData)
    {
        boolean isNotesUpdated = false;
        try {
            obj.generateDataForUpdateNotes();
            for (int i = 0; i < notesTestData.length; i++)
            {
                PageHelper.invisibilityOfElement(driver, loader);
                PageHelper.javascriptClick(driver, notesMenu);
                PageHelper.javascriptClick(driver,clickFirstNotes);
                PageHelper.javascriptClick(driver,editButtonForFirstNotes);
                PageHelper.invisibilityOfElement(driver, loader);
                PageHelper.sendKeysToElement(driver, notesArea, notesTestData[i].get("Notes"));
                if(notesTestData[i].containsKey("Attachment")) {
                    File f = new File(notesTestData[i].get("Attachment"));
                    PageHelper.uploadFile(driver, uploadAttachment, f.getAbsolutePath());
                    PageHelper.invisibilityOfElement(driver, loader);
                }
                PageHelper.javascriptClick(driver, updateButtonForNotes);

                if(isNotesSuccessfullyUpdated())
                {
                    isNotesUpdated =true;
                }
                else {
                    isNotesUpdated=false;
                    break;
                }

            }
        }
        catch (Exception e)
        {
            Assert.fail(String.valueOf(e));
            return isNotesUpdated;
        }

        return  isNotesUpdated;
    }
            public boolean isNotesSuccessfullyCreated()
        {
            return PageHelper.validateConfirmationMessage(driver, notesCreationMessage);
        }

    public boolean isNotesSuccessfullyUpdated()
    {
        return PageHelper.validateConfirmationMessage(driver, notesUpdateMessage);
    }

    public boolean isNotesSuccessfullyDeleted()
    {
        return PageHelper.validateConfirmationMessage(driver, notesDeleteMessage);
    }

    public boolean isFileAlertDisplayed()
    {
        return PageHelper.validateConfirmationMessage(driver, invalidFileAlertMessage);
    }

    public <T extends BaseData> boolean addNotesNegative(T obj, HashMap<String, String>[] notesTestData,  HashMap<String, String>[] notesValidationMessages)
    {
        boolean isMessageDisplayed = false;
        try {
            obj.generateDataForCreateNotesNegativeTesting();
            obj.generateAddNotesValidationMessages();
            for (int i = 0; i < notesTestData.length; i++)
            {
                System.out.println("Iteration is "+i);
                Thread.sleep(2000);
                PageHelper.javascriptClick(driver,notesMenu);
                PageHelper.invisibilityOfElement(driver,loader);
                PageHelper.javascriptClick(driver, newNoteButton);
                PageHelper.invisibilityOfElement(driver, loader);
                PageHelper.sendKeysToElement(driver, notesArea, notesTestData[i].get("Notes"));
                createNoteLabel.click();
                Thread.sleep(1000);
                if(notesTestData[i].containsKey("Attachment"))
                {
                    File f = new File(notesTestData[i].get("Attachment"));
                    PageHelper.uploadFile(driver, uploadAttachment, f.getAbsolutePath());
                    PageHelper.invisibilityOfElement(driver, loader);
                }
                if(notesValidationMessages[i].containsKey("Notes") &&(notesValidationMessages[i].containsKey("File Type Error")))
                {
                    boolean fileAlertStatus = isFileAlertDisplayed();
                    if(getAllErrorMessages().contains(notesValidationMessages[i].get("Notes")) && fileAlertStatus == true)
                    {

                        if(PageHelper.isButtonEnabled(driver, addNotesButton))
                        {
                            PageHelper.invisibilityOfElement(driver,loader);
                            PageHelper.javascriptClick(driver,closeButtonInForm);
                            PageHelper.invisibilityOfElement(driver,notesForm);
                            isMessageDisplayed = false;
                            break;
                        }
                        else {
                           
                            isMessageDisplayed = true;
                        }
                    }
                    else
                    {
                        isMessageDisplayed = false;
                        PageHelper.invisibilityOfElement(driver,loader);
                        PageHelper.javascriptClick(driver,closeButtonInForm);
                        PageHelper.invisibilityOfElement(driver,notesForm);
                        break;
                    }

                  }
             else if(notesValidationMessages[i].containsKey("Notes") &&!(notesValidationMessages[i].containsKey("File Type Error")))
                 {
                if(getAllErrorMessages().contains(notesValidationMessages[i].get("Notes")))
                {
                    if(PageHelper.isButtonEnabled(driver, addNotesButton))
                    {
                       
                        isMessageDisplayed = false;
                        PageHelper.invisibilityOfElement(driver,loader);
                        PageHelper.javascriptClick(driver,closeButtonInForm);
                        PageHelper.invisibilityOfElement(driver,notesForm);
                        break;
                    }
                    else {
                       
                        isMessageDisplayed = true;
                    }
                }
                else
                {
                    isMessageDisplayed = false;
                    PageHelper.invisibilityOfElement(driver,loader);
                    PageHelper.javascriptClick(driver,closeButtonInForm);
                    PageHelper.invisibilityOfElement(driver,notesForm);
                    break;
                }
             }
             else if (!(notesValidationMessages[i].containsKey("Notes")) &&(notesValidationMessages[i].containsKey("File Type Error")))
             {
                     if(isFileAlertDisplayed())
                     {
                         isMessageDisplayed =true;
                     }
                     else {
                        
                         isMessageDisplayed = false;
                         PageHelper.invisibilityOfElement(driver,loader);
                         PageHelper.javascriptClick(driver,closeButtonInForm);
                         PageHelper.invisibilityOfElement(driver,notesForm);
                         break;
                     }
                 }
                PageHelper.invisibilityOfElement(driver,loader);
                PageHelper.javascriptClick(driver,closeButtonInForm);
                PageHelper.invisibilityOfElement(driver,notesForm);

            }


        }

        catch (Exception e)
        {
            Assert.fail(String.valueOf(e));
            return isMessageDisplayed;
        }

        return  isMessageDisplayed;
    }

    public <T extends BaseData> boolean editNotesNegative(T obj, HashMap<String, String>[] notesTestData,  HashMap<String, String>[] notesValidationMessages)
    {
        boolean isMessageDisplayed = false;
        try {
            obj.generateDataForEditNotesNegativeTesting();
            obj.generateEditNotesValidationMessages();
            for (int i = 0; i < notesTestData.length; i++)
            {
                System.out.println("Iteration is " +i);
                PageHelper.invisibilityOfElement(driver,loader);
                PageHelper.javascriptClick(driver, notesMenu);
                PageHelper.javascriptClick(driver,clickFirstNotes);
                PageHelper.javascriptClick(driver,editButtonForFirstNotes);
                PageHelper.invisibilityOfElement(driver, loader);
                PageHelper.sendKeysToElement(driver, notesArea, notesTestData[i].get("Notes"));
                updateNoteLabel.click();
                if(notesTestData[i].containsKey("Attachment"))
                {
                    File f = new File(notesTestData[i].get("Attachment"));
                    PageHelper.uploadFile(driver, uploadAttachment, f.getAbsolutePath());
                    PageHelper.invisibilityOfElement(driver, loader);
                }
                if(notesValidationMessages[i].containsKey("Notes") &&(notesValidationMessages[i].containsKey("File Type Error")))
                {
                boolean fileAlertStatus = isFileAlertDisplayed();
                if(getAllErrorMessages().contains(notesValidationMessages[i].get("Notes")) && fileAlertStatus == true)
                {
                    if(PageHelper.isButtonEnabled(driver, updateButtonForNotes))
                    {
                        PageHelper.invisibilityOfElement(driver,loader);
                        PageHelper.javascriptClick(driver,closeButtonInForm);
                        PageHelper.invisibilityOfElement(driver,notesForm);
                        isMessageDisplayed = false;
                        break;
                    }
                    else {

                        isMessageDisplayed = true;
                    }
                }
                    else
                    {

                        isMessageDisplayed = false;
                        PageHelper.invisibilityOfElement(driver,loader);
                        PageHelper.javascriptClick(driver,closeButtonInForm);
                        PageHelper.invisibilityOfElement(driver,notesForm);
                        break;
                    }

                }
                else if(notesValidationMessages[i].containsKey("Notes") &&!(notesValidationMessages[i].containsKey("File Type Error")))
                {
                    if(getAllErrorMessages().contains(notesValidationMessages[i].get("Notes")))
                    {
                        if(PageHelper.isButtonEnabled(driver, updateNotesButton))
                        {

                            isMessageDisplayed = false;
                            PageHelper.invisibilityOfElement(driver,loader);
                            PageHelper.javascriptClick(driver,closeButtonInForm);
                            PageHelper.invisibilityOfElement(driver,notesForm);
                            break;
                        }
                        else {

                            isMessageDisplayed = true;
                        }
                    }
                    else
                    {
                        isMessageDisplayed = false;
                        Thread.sleep(2000);
                        PageHelper.invisibilityOfElement(driver,loader);
                        PageHelper.javascriptClick(driver,closeButtonInForm);
                        PageHelper.invisibilityOfElement(driver,notesForm);
                        break;
                    }
                }
                else if (!(notesValidationMessages[i].containsKey("Notes")) &&(notesValidationMessages[i].containsKey("File Type Error")))
                {
                    if(isFileAlertDisplayed())
                    {
                        isMessageDisplayed =true;
                    }
                    else
                    {
                        isMessageDisplayed = false;
                        PageHelper.invisibilityOfElement(driver,loader);
                        PageHelper.javascriptClick(driver,closeButtonInForm);
                        PageHelper.invisibilityOfElement(driver,notesForm);
                        break;
                    }
                }
                PageHelper.invisibilityOfElement(driver,loader);
                PageHelper.javascriptClick(driver,closeButtonInForm);
                PageHelper.invisibilityOfElement(driver,notesForm);
            }


        }

        catch (Exception e)
        {
            Assert.fail(String.valueOf(e));
            return isMessageDisplayed;
        }

        return  isMessageDisplayed;
    }
    public boolean validateErrors(HashMap<String, String> notesValidationMessage, ArrayList<String> capturedMessages) {
        boolean isErrorPresent = false;
        for (Map.Entry<String, String> entry : notesValidationMessage.entrySet())
        {
            String value = entry.getValue();
            for (String ele : capturedMessages)
            {
                if (value.contains(ele))
                {
                    isErrorPresent = true;
                    break;
                }
            }
            //isErrorPresent = false;
        }

        return isErrorPresent;
    }

        public ArrayList<String> getAllErrorMessages()
    {

            List<WebElement> errorMessages = driver.findElements(By.xpath("//mat-error[@role='alert']"));
            ArrayList<String> message = new ArrayList<>();
            for (WebElement e : errorMessages) {
                message.add(e.getText());
            }
            System.out.println(message);
            return message;

        }
}