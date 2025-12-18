//***********************************************************************************
//* Description
//*------------
//* Edit plant test
//***********************************************************************************
//*
//* Author           : SIVABALAN RAHUL
//* Date Written     : 22/02/2023
//* 
//*
//* 
//* Test Case Number       Date         Author        Comments
//* ================       ====         =====        ========
//*                        22/02/2023   RAHUL.S    Orginal Version
//*
//************************************************************************************

package com.invicta.qa.testcases.sbu;

import java.io.FileInputStream;
import java.io.IOException;

import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.apache.xmlbeans.impl.xb.xsdschema.Public;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.Point;
import org.openqa.selenium.support.PageFactory;
import org.testng.Assert;
import org.testng.AssertJUnit;
import org.testng.annotations.Test;

import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.Status;
import com.invicta.qa.base.DriverIntialization;
import com.invicta.qa.pages.login.Loginpg;
import com.invicta.qa.pages.sbu.EditPlantPage;

public class EditPlant extends DriverIntialization {
    
	private static final String Expect = null;
	static String fieldValue = "";
//********************************************************************************************************
//                          THE METHOD IS FOR GENERATING REPORT 
//********************************************************************************************************	
	public static void TestCasePrint(String TestCaseName, String expectedValue, String actualValue) {
		boolean position = true;
		ExtentTest testCase = extent.createTest(TestCaseName);
		try {
			AssertJUnit.assertEquals(actualValue, expectedValue);
		} catch (AssertionError e) {
			position = false;
		}
		if (position) {
			testCase.log(Status.INFO, "Actualvalue :- " + actualValue);
			testCase.log(Status.INFO, "Expectedvalue :- " + expectedValue);
			testCase.log(Status.INFO, "Correct value");
			testCase.log(Status.PASS, actualValue);
		} else {
			testCase.log(Status.INFO, "Actualvalue :- " + actualValue);
			testCase.log(Status.INFO, "ExpectedValue :- " + expectedValue);
			testCase.log(Status.INFO, "wrong value");
			testCase.log(Status.FAIL, actualValue);
		}

	}
//********************************************************************************************************
//********************************************************************************************************
       
	@Test
	public static void clickeditplant() throws InterruptedException, IOException {
//********************************************************************************************************		
// THIS METHOD IS FOR LOGIN AND CLICKING THE MASTER 
//********************************************************************************************************		
		Loginpg.login();
		Thread.sleep(4000);
//********************************************************************************************************	
		
		
//********************************************************************************************************		
//	                                  AFTER CLICKING MASTER TO PLANT
//********************************************************************************************************		
		EditPlantPage editplantpg = new EditPlantPage();
		PageFactory.initElements(driver, editplantpg);
		Thread.sleep(3000);
		FinaleditPlant.search();
//		EditPlantPage.clickplant.click();
		Thread.sleep(3000);
		
//********************************************************************************************************		
//                                   STEP-02 -- CHECKING EDIT PLANT ICON 	
//********************************************************************************************************		
		testCase = extent.createTest("CHECKING UI OF EDIT ICON");
		boolean Value1 = EditPlantPage.EditPlantIcon.isDisplayed();

		if (Value1) {

			try {
				boolean Value = EditPlantPage.EditPlantIcon.isDisplayed();
				// Thread.sleep(2000);
				TestCasePrint("VISIBILITY", "true", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("VISIBILITY", "true", String.valueOf(e));
			}
		
		try {
			boolean value = EditPlantPage.EditPlantIcon.isEnabled();

			TestCasePrint("EDIT ICON ENABLE", "true", String.valueOf(value));
		} catch (Exception e) {
			TestCasePrint("EDIT ICON ENABLE", "true", String.valueOf(e));

		}
		EditPlantPage.EditPlantIcon.click();
		} else {
			TestCasePrint("ICON IS NOT DISPLAYED", "true", String.valueOf(Value1));
		}
		
//*******************************************get the text in disabled field****************************************************
//		String fieldValue = (String) ((JavascriptExecutor) driver).executeScript("return arguments[0].value;", EditPlantPage.mandatory);
//		System.out.println("disabled " + fieldValue);
//*********************************************************************************************************************************

//*********************************************************************************************************************************		
// checking mandatory and get report
//*********************************************************************************************************************************		
		checkfirstfield();

//*********************************************************************************************************************************	
//*********************************************************************************************************************************		
// checking mandatory and get report
//*********************************************************************************************************************************		
		PlantNameEdit();
		checkUpdateButton();
		ClickUpdateButton();
	//	confirmUpdate();
		logout();
	}
	
//*****************************************************************************************************************************	
//							STEP-03 -- CHECK THE MANDATORY FILED IS DISABLED 
//	***************************************************************************************************************************
	
	public static void checkfirstfield() throws InterruptedException, IOException {
		// test Enabled
		try {
			boolean value = EditPlantPage.mandatory.isEnabled();

			TestCasePrint("STEP-03 -- CHECK THE MANDATORY FILED IS DISABLED  ", "false", String.valueOf(value));
		} catch (Exception e) {
			TestCasePrint("STEP-03 -- CHECK THE MANDATORY FILED IS DISABLED", "false", String.valueOf(e));

		}

	}
//*****************************************************************************************************************************	
// 												EDIT THE PLANT NAME 
//*****************************************************************************************************************************		
	public static void PlantNameEdit() throws InterruptedException, IOException {
		// Thread.sleep(4000);
//		EditPlant_page editplantpg = new EditPlant_page();
//		PageFactory.initElements(driver, editplantpg);
//		FileInputStream file = new FileInputStream(System.getProperty("C:\\Users\\hp\\eclipse-workspace\\AddSbu\\src\\test\\resources\\Excel-sheets\\SampleExcel.xlsx"));
//		
//		XSSFWorkbook workbook = new XSSFWorkbook(file);
//		
//		XSSFSheet sheet = workbook.getSheet("EditPlant");
//
//		int rowcount = sheet.getLastRowNum();
//		for (int i = 0; i <= rowcount; i++) {
//			XSSFRow row = sheet.getRow(0);
//
//			String Plant = (String) row.getCell(0).getStringCellValue();
//			String Address = (String) row.getCell(1).getStringCellValue();
//			String ContactNo = (String) row.getCell(2).getStringCellValue();
//			String Fax = (String) row.getCell(3).getStringCellValue();
//			String Description = (String) row.getCell(4).getStringCellValue();
//			
//			EditPlant_page.plantname.sendKeys(Plant);
//			EditPlant_page.plantname.sendKeys(Address);
//			EditPlant_page.plantname.sendKeys(ContactNo);
//			EditPlant_page.plantname.sendKeys(Fax);
//			EditPlant_page.plantname.sendKeys(Description);
		
		// for plant name
		Thread.sleep(1500);
		try {
		EditPlantPage.plantname.sendKeys(Keys.CONTROL + "a", Keys.DELETE);
		EditPlantPage.plantname.sendKeys("RMC Balangoda Plant");
		}catch(Exception e) {
			testCase = extent.createTest("PLANT NAME IS NOT WENT");
		}
//		// for address
//		try {
//		EditPlantPage.Address.sendKeys(Keys.CONTROL + "a", Keys.DELETE);
//		EditPlantPage.Address.sendKeys("No.4,Kokkuvil,Jaffna");
//		}catch(Exception e) {
//			testCase = extent.createTest("Address did not went");
//		}
//		// for Contact No
//		try {
//		EditPlantPage.ContactNo.sendKeys(Keys.CONTROL + "a", Keys.DELETE);
//		EditPlantPage.ContactNo.sendKeys("0766450923");
//		}catch(Exception e) {
//			testCase = extent.createTest("Contact No did not went");
//		}
//		// for fax
//		try {
//		EditPlantPage.fax.sendKeys(Keys.CONTROL + "a", Keys.DELETE);
//		EditPlantPage.fax.sendKeys("9466450921");
//		}catch(Exception e) {
//			testCase = extent.createTest("Fax did not went");
//		}
//		Thread.sleep(2000);
//		// for SubBusiness drop down
//		try {
//		EditPlantPage.ClickSubBusinessUnitDropDown.click();
//		}catch(Exception e) {
//			testCase = extent.createTest("Sub Business Unit Dropdown selection wrong ");
//		}
//		Thread.sleep(2000);
//		try {
//		EditPlantPage.SelectSubBusiness.click();
//		}catch(Exception e) {
//			testCase = extent.createTest("Sub Business Unit Dropdown selection wrong ");
//		}
//		// for plant manager
//		Thread.sleep(2000);
//		try {
//		EditPlantPage.PlantManagerDropDown.click();
//		}catch(Exception e) {
//			testCase = extent.createTest("Plant manager Dropdown selection wrong");
//		}
//		Thread.sleep(2000);
//		try {
//		EditPlantPage.SelectPlantManager.click();
//		}catch(Exception e) {
//			testCase = extent.createTest("Plant manager Dropdown selection wrong");
//		}
//		Thread.sleep(2000);
//		// for description
//		try {
//		EditPlantPage.Description.sendKeys(Keys.CONTROL + "a", Keys.DELETE);
//		Thread.sleep(2000);
//		EditPlantPage.Description.sendKeys("RMC Jaffna Plant");
//		}catch(Exception e) {
//			testCase = extent.createTest("Description did not went");
//		}

	}
//*************************************************************************************************************
//									STEP-04-CHECKING UI OF UPDATE BUTTON"	
//*************************************************************************************************************

	public static void checkUpdateButton() throws InterruptedException, IOException {

		testCase = extent.createTest("STEP-04-CHECKING UI OF UPDATE BUTTON");
		boolean Value1 = EditPlantPage.UpdateButton.isDisplayed();

		if (Value1) {

			try {
				boolean Value = EditPlantPage.UpdateButton.isDisplayed();
				// Thread.sleep(2000);
				TestCasePrint("1)UPDATE BUTTON IS DISPLAYED", "true", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("1)UPDATE BUTTON IS DISPLAYED", "true", String.valueOf(e));
			}

			try {
				boolean Value = EditPlantPage.UpdateButton.isEnabled();
				// Thread.sleep(2000);
				TestCasePrint("2)UPDATE BUTTON IS ENABLED", "true", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("2)UPDATE BUTTON IS ENABLED", "true", String.valueOf(e));
			}

			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("background-color");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("3)UPDATE BUTTON background-color", "rgba(0, 19, 40, 1)", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("3)UPDATE BUTTON background-color", "rgba(0, 19, 40, 1)", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("padding");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("4)UPDATE BUTTON UI - padding", "4px 15px", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("4)UPDATE BUTTON UI - padding", "4px 15px", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("font-family");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("5)UPDATE BUTTON UI - font-family", "Roboto, sans-serif", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("5)UPDATE BUTTON UI - font-family", "Roboto, sans-serif", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("color");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("6)UPDATE BUTTON UI - color", "rgba(255, 255, 255, 1)", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("6)UPDATE BUTTON UI - color", "rgba(255, 255, 255, 1)", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("font-size");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("7)UPDATE BUTTON  UI - font-size", "14px", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("7)UPDATE BUTTON UI - font-size", "14px", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("border-radius");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("8)UPDATE BUTTON UI -border-radius", "2px", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("8)UPDATE BUTTON UI - border-radius", "2px", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("border-color");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("9)UPDATE BUTTON  UI -border-color", "rgb(255, 255, 255)", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("9)UPDATE BUTTON UI -border-color", "rgb(255, 255, 255)", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("box-shadow");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("10)UPDATE BUTTON UI -box-shadow", "rgba(0, 0, 0, 0.016) 0px 2px 0px 0px", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("10)UPDATE BUTTON UI - box-shadow", "rgba(0, 0, 0, 0.016) 0px 2px 0px 0px", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("font-weight");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("11)UPDATE BUTTON  UI -font-weight", "400", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("11)UPDATE BUTTON UI - font-weight", "400", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("cursor");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("12)UPDATE BUTTON UI -cursor", "pointer", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("12)UPDATE BUTTON UI - cursor", "pointer", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getCssValue("opacity");
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("13)UPDATE BUTTON UI -opacity", "1", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("13)UPDATE BUTTON UI -opacity", "1", String.valueOf(e));
			}
			try {
				String Value = EditPlantPage.UpdateButton.getText();
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("14)UPDATE BUTTON UI -text spelling", "Update", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("14)UPDATE BUTTON UI -text spelling", "Update", String.valueOf(e));
			}
			try {
				Dimension Value = EditPlantPage.UpdateButton.getSize();
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("15)UPDATE BUTTON UI -Size", "(74, 32)", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("15)UPDATE BUTTON UI -Size", "(74, 32)", String.valueOf(e));
			}

			try {
				Point Value = EditPlantPage.UpdateButton.getLocation();
				System.out.println(Value);
				// Thread.sleep(2000);
				TestCasePrint("16)UPDATE BUTTON  UI -position", "(887, 670)", String.valueOf(Value));
			} catch (Exception e) {
				TestCasePrint("16)UPDATE BUTTON UI -position", "(887, 670)", String.valueOf(e));
			}

		} else {
			TestCasePrint("ELEMENT IS NOT DIPLAYED", "true", String.valueOf(Value1));
		}

	}
//*************************************************************************************************************
	
	public static void ClickUpdateButton() throws InterruptedException,IOException{
		try {
		EditPlantPage.UpdateButton.click();
		testCase = extent.createTest("STEP-05 --CONFIRM THE CLICKED UPDATE BUTTON");
		}catch (Exception e) {
			testCase = extent.createTest("STEP-05--UPDATE BUTTON DID NOT CLICKED");
		}
	}

//	public static void confirmUpdate() throws InterruptedException,IOException {
//		Thread.sleep(2000);
//	//	System.out.println(Code);
//	//	String conformUpdate = EditPlantPage.confirmUpdate.getText();
//		try {
//			String conformUpdate = EditPlantPage.confirmUpdate.getText();
//			//System.out.println(fieldValue);
//			String Expect ="AB RMC Balangoda Plant Sbuone Sarath No.4,Kokkuvil,Jaffna 0766450923 9466450921";
//			System.out.println("After edit " + conformUpdate);
//			 Thread.sleep(2000);
//			TestCasePrint("confirm Update",Expect, String.valueOf(conformUpdate));
//		} catch (Exception e) {
//			TestCasePrint("confirm Update",Expect, String.valueOf(e));
//		}	
//	}


	
	// Quits the browser and closes all the windows
	public static void logout() throws InterruptedException,IOException{
//		Thread.sleep(3000);
//		EditPlantPage.admin.click();
//		Thread.sleep(3000);
//		EditPlantPage.logout.click();
		driver.quit();
	}
		
//	}
}








