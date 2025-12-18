package com.ict.tests;

import java.time.Duration;

import org.apache.poi.ss.util.NumberToTextConverter;
import org.testng.Assert;
import org.testng.annotations.Test;

import com.ict.constants.AutomationConstants;
import com.ict.pages.LoginVerification;
import com.ict.pages.AddEmployeeClass;
import com.ict.pages.ListOfEmployees;
import com.ict.pages.LoginPage;
import com.ict.utilities.ExcelUtilities;

public class NewTest extends BaseClass {
	
	LoginPage logobj;
	LoginVerification homeobj;
	AddEmployeeClass addobj;
	ListOfEmployees listobj;
	
  @Test(priority=1)
  public void credentialsVerification() throws Exception {
	  
	        logobj=new LoginPage(getDriver());
	        homeobj=new LoginVerification(getDriver());
	        
			String actualusername=ExcelUtilities.readDetails(0, 0).getStringCellValue();
			logobj.getUsername(actualusername);
			Assert.assertEquals(AutomationConstants.expusername, actualusername);
			
			String actualpassword=NumberToTextConverter.toText(ExcelUtilities.readDetails(1, 0).getNumericCellValue());
			logobj.getPassword(actualpassword);
			Assert.assertEquals(AutomationConstants.exppassword, actualpassword);
			
			logobj.setClick();
			
			  String actualText=homeobj.loginVerification();
			  Assert.assertEquals(AutomationConstants.checklogin, actualText);
			  System.out.println("Redirected to new page");
		}
  @Test(priority=2)
  public void addEmployee()throws Exception
  {
	  addobj=new AddEmployeeClass(getDriver());
	  
	  addobj.addEmployee();
	  
	  addobj.clickAddEmployee();
	  
	  String actualname=ExcelUtilities.readDetails(2, 0).getStringCellValue();
	  addobj.sendName(actualname);
	  Assert.assertEquals(AutomationConstants.expname, actualname);
	  
	  String actualpassword=ExcelUtilities.readDetails(3, 0).getStringCellValue();
	  addobj.sendPassword(actualpassword);
	  Assert.assertEquals(AutomationConstants.exppassword1, actualpassword);
	  
	  String actualemail=ExcelUtilities.readDetails(4, 0).getStringCellValue();
	  addobj.sendEmail(actualemail);
	  Assert.assertEquals(AutomationConstants.expemail, actualemail);
	  
	  addobj.sendDesignation();
	  
	  addobj.sendReporting();
	  
	  addobj.sendMember();
	  
	  String actualempid=NumberToTextConverter.toText(ExcelUtilities.readDetails(5, 0).getNumericCellValue());
	  addobj.sendEmpid(actualempid);
	  Assert.assertEquals(AutomationConstants.expempid, actualempid);
	  
	  String actualconfirmpassword=ExcelUtilities.readDetails(6, 0).getStringCellValue();
	  addobj.sendConfirmpassword(actualconfirmpassword);
	  Assert.assertEquals(AutomationConstants.expconfirmpassword, actualconfirmpassword);
	  
	  String actualphone=NumberToTextConverter.toText(ExcelUtilities.readDetails(7, 0).getNumericCellValue());
	  addobj.sendPhone(actualphone);
	  Assert.assertEquals(AutomationConstants.expphone,actualphone);
	  
	  addobj.sendEmptype();
	  
	  addobj.clickCheck();
	  
	  String actualaddress=ExcelUtilities.readDetails(8, 0).getStringCellValue();
	  addobj.sendAddress(actualaddress);
	  Assert.assertEquals(AutomationConstants.expaddress, actualaddress);
	  
	  addobj.click();
			  

  }
  
  @Test(priority=3)
  public void listEmployees() throws Exception
  {
	  listobj=new ListOfEmployees(getDriver());
	  listobj.addEmployee();
	  listobj.clickListEmployee();
	  listobj.pageClick();
	  
	  listobj.clickEdit();
	  
	  String actualnewempid=NumberToTextConverter.toText(ExcelUtilities.readDetails(10, 0).getNumericCellValue());
	  listobj.editEmpid(actualnewempid);
	  Assert.assertEquals(AutomationConstants.expnewempid, actualnewempid);
	  
	  listobj.clickupdate();
	  listobj.clickdelete();
	  
  }
  }
  
  
  
  
