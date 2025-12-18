package dataProviderPractice;

import java.io.FileInputStream;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.DataFormatter;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import smsGenericUtilities.ExcelUtility;
import smsGenericUtilities.IPathconstants;

public class DataPtoviderExcelPractice {
	
	//read the data from data provider using hard coding
	@Test(dataProvider = "readDataFromExcel")
	public void displayData(String Phone,String model,String colour,String price,String discout)
	{
		System.out.println(Phone+"\t"+model+"\t"+colour+"\t"+price+"\t"+discout);
	}

	
	@DataProvider
	public Object[][] readDataFromExcel() throws Throwable
	{
		FileInputStream fis=new FileInputStream(IPathconstants.excelFilePath);
		Workbook wb=WorkbookFactory.create(fis);
		Sheet sh=wb.getSheet("dataProvider");
		int lastRow=sh.getLastRowNum();
		int lastCell=sh.getRow(lastRow).getLastCellNum();
		System.out.println(lastRow+" "+lastCell);
		Object[][] arr=new Object[lastRow][lastCell];
		DataFormatter df=new DataFormatter();
		
	for(int i=0;i<lastRow;i++)
	{
		for(int j=0;j<lastCell;j++)
		{
			Cell cell=sh.getRow(i+1).getCell(j);
			arr[i][j]=df.formatCellValue(cell);
		}
	}
	
	return arr;
		
	}
	
	
	//read the data from other class data provider using hard coding
		@Test(dataProviderClass = Practice.class,dataProvider = "readDataFromExcel1")
		public void displayData1(String Phone,String model,String colour,String price,String discout)
		{
			System.out.println(Phone+"\t"+model+"\t"+colour+"\t"+price+"\t"+discout);
		}
		
		
		
		
		
		
		
		//read the data from excel using dataprovider
		@Test(dataProvider = "fetchdataFromExcel")
		public void displayData2(String Phone,String model,String colour,String price,String discout)
		{
			System.out.println(Phone+"\t"+model+"\t"+colour+"\t"+price+"\t"+discout);
		}
		
		@DataProvider
		public Object[][] fetchdataFromExcel() throws Throwable
		{
			ExcelUtility eutil=new ExcelUtility();
			Object[][] arr=eutil.fetchDataFromExcelGiveItToDataProvider("dataProvider");
			return arr;
		}
		
		
}
