package homeScripts;
import java.io.IOException;

import java.util.Set;

import org.apache.poi.EncryptedDocumentException;

import org.openqa.selenium.interactions.Actions;

import org.testng.Reporter;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Listeners;
import org.testng.annotations.Test;

import action.ScrollDown;
import base.CrossBrowserTesting;
import fileUtility.GetExcelData;
import pageObjectModel.HomePOM;
@Listeners(listeners.ListenersClass.class)
public class ValidateEmail extends CrossBrowserTesting
{
	
	@DataProvider(name = "excelData")
	public Object[][] getData() throws IOException 
	{
		int row = GetExcelData.getRows("Sheet1");
		System.out.println(row);
		int column = GetExcelData.getCells("Sheet1");
		System.out.println(column);
      Object[][]obj=new Object[row][column];
      for(int i=0; i<row; i++)
      {
    	  for(int j=0; j<column; j++)
    	  {
    	 obj[i][j]= GetExcelData.Exceldata("Sheet1", i, j); 
    	  }
      }
      return obj;
      
      }
	@Test(enabled= true, dataProvider = "excelData")
	  public void emailValidation(String data1, String data2) throws EncryptedDocumentException, IOException, InterruptedException
	  {
		  HomePOM hp = new HomePOM(driver);
		 
		  ScrollDown.scrollPage(hp.email);
		  
		  Thread.sleep(5000); 
		  hp.email.sendKeys(data1);
		  Thread.sleep(3000);                          
		  hp.subscribe.click();
		  
		if(hp.errorMail.isDisplayed()|| driver.getCurrentUrl().equals("https://metapercept.com/"))
		{
			Reporter.log("Email field does not accept the invalid email format",true);
		}
		else {
		  
		    String given_title = "Metapercept Technology Services LLP";
			
			
			Set<String> child = driver.getWindowHandles();
		
			Thread.sleep(4000);
			
			for(String str : child)
			{
				driver.switchTo().window(str);
				
				if(given_title.equals(driver.getTitle()))
				{
		       if(hp.thankUPage.isDisplayed())
		       {
			     Reporter.log("Email field accepts the valid email format",true);
		       }
			    }
				
		   }
	       }
	  }
	
	  
	  
}
