package Pom;



	import java.awt.AWTException;
	import java.awt.Robot;
	import java.io.File;
	import java.io.FileInputStream;
	import java.io.FileNotFoundException;
	import java.io.FileOutputStream;
	import java.io.IOException;
	import java.util.List;
	import java.util.Set;
	import java.util.concurrent.TimeUnit;

	import org.apache.commons.io.FileUtils;
	import org.apache.poi.ss.usermodel.Cell;
	import org.apache.poi.ss.usermodel.Row;
	import org.apache.poi.ss.usermodel.Sheet;
	import org.apache.poi.ss.usermodel.Workbook;
	import org.apache.poi.xssf.usermodel.XSSFWorkbook;
	import org.openqa.selenium.Alert;
	import org.openqa.selenium.By;
	import org.openqa.selenium.JavascriptExecutor;
	import org.openqa.selenium.Keys;
	import org.openqa.selenium.OutputType;
	import org.openqa.selenium.TakesScreenshot;
	import org.openqa.selenium.WebDriver;
	import org.openqa.selenium.WebElement;
	import org.openqa.selenium.chrome.ChromeDriver;
	import org.openqa.selenium.interactions.Actions;
	import org.openqa.selenium.support.ui.Select;

	import io.github.bonigarcia.wdm.WebDriverManager;

	public class BaseCode {
		
			public static WebDriver driver;	// instance variable (because "WebDriver driver;" this is what we are going to
			static Actions act;
			static Alert alert; // use all the method.)
			static Robot rb;
			static TakesScreenshot screenShot;

			public static void driverLaunch(String url) throws AWTException {
				
				// Driver Launch
				WebDriverManager.chromedriver().setup();
				driver = new ChromeDriver();
				act = new Actions(driver);
				rb = new Robot();
				driver.get(url);
				screenShot = (TakesScreenshot) driver;

			}

			// Maximize the window
			public static void maximizeMethod() {
				driver.manage().window().maximize();
			}

			// implicit Waits
			public static void implicitwait(long time) {
				driver.manage().timeouts().implicitlyWait(time, TimeUnit.SECONDS);

			}

			public static void quitDriver() {
				driver.quit();
			}

			public void closeTab() {
				driver.close();
			}

			public void click(WebElement element) {
				element.click();

			}
			public void clearMethod(WebElement element) {
			element.clear();	

			}
			
			
			public String getTextMethod(WebElement element) {
				String text = element.getText();
				return text;

			}
			public String getAttributeValue(WebElement element, String name) {
				String attribute = element.getAttribute(name);
				return attribute;

			}

			// Without X'path
			public WebElement findelementsById(String Id) {
				WebElement element = driver.findElement(By.id(Id));
				return element;

			}

			public List<WebElement> findelements(By listofElements) {
				List<WebElement> elements = driver.findElements(listofElements);
				return elements;
			}

			public WebElement findelementTagname(String tagName) {
				WebElement element = driver.findElement(By.tagName(tagName));
				return element;
			}

			public WebElement fidelementClassname(String className) {
				WebElement element = driver.findElement(By.className(className));
				return element;
			}

			public static void sendKeysTxt(WebElement element, String text) {
				element.sendKeys(text);
			}
			
			// Take the data from the excel sheet
			public static String getData(String sheetName, int rownum, int cellnum) throws IOException {
				File file = new File("C:\\Users\\Herbert\\eclipse-workspace\\SampleOne\\Output\\Data.xlsx");
				FileInputStream input = new FileInputStream(file);
				Workbook book = new XSSFWorkbook(input);
				Sheet sheet = book.getSheet(sheetName);
				Row row = sheet.getRow(rownum);
				Cell cell = row.getCell(cellnum);
				String stringCellValue = cell.getStringCellValue();
				return stringCellValue;
			}

			// Give the data to excel sheet
			public static FileOutputStream putData(String sheetName, String cellvalue, int rownum, int cellnum)
					throws IOException {
				File file = new File("C:\\Users\\Herbert\\eclipse-workspace\\SampleOne\\Output\\Data.xlsx");
				Workbook book = new XSSFWorkbook();
				Sheet Sheet = book.createSheet(sheetName);
				Row Row = Sheet.createRow(rownum);
				Cell Cell = Row.createCell(cellnum);
				Cell.setCellValue(cellvalue);
				FileOutputStream out = new FileOutputStream(file);
				book.write(out);
				return out;
			}
			
			// New sheet creation in existing excel sheet 
			
			public static void main(String sheetName, String cellvalue, int rownum, int cellnum) throws IOException {
				File file = new File("C:\\Users\\Herbert\\eclipse-workspace\\SampleOne\\Output\\Data.xlsx");
				FileInputStream input = new FileInputStream(file);
				Workbook book = new XSSFWorkbook(input);
				Sheet createSheet = book.createSheet(sheetName);
				Row createRow = createSheet.createRow(rownum);
				Cell createCell = createRow.createCell(cellnum);
				createCell.setCellValue(cellvalue);
				FileOutputStream out = new FileOutputStream(file);
				book.write(out);
			}

			// With X'path
			public WebElement xpathAttValue(String by) {
				WebElement element = driver.findElement(By.xpath(by));
				return element;
			}

			public WebElement xpathusingIndex(String usingindex) {
				WebElement element = driver.findElement(By.xpath(usingindex));
				return element;
			}

			public WebElement xpathusingTxt(String text) {
				WebElement element = driver.findElement(By.xpath(text));
				return element;
			}

			public WebElement xpathusingContains(String containsTxt) {
				WebElement element = driver.findElement(By.xpath(containsTxt));
				return element;
			}

			public WebElement xpathcontainsAttri(String containsAttribute) {
				WebElement element = driver.findElement(By.xpath(containsAttribute));
				return element;
			}

			public WebElement startswithAttri(String startingAttValue) {
				WebElement element = driver.findElement(By.xpath(startingAttValue));
				return element;
			}

			public WebElement startswithTxt(String startintxtValue) {
				WebElement element = driver.findElement(By.xpath(startintxtValue));
				return element;
			}

			public WebElement andXpath(String andxpath) {
				WebElement element = driver.findElement(By.xpath(andxpath));
				return element;
			}

			public WebElement orXpath(String orxpath) {
				WebElement element = driver.findElement(By.xpath(orxpath));
				return element;
			}

			public WebElement multipleAttribute(String multipleAttri) {
				WebElement element = driver.findElement(By.xpath(multipleAttri));
				return element;
			}

			public WebElement unknownTagname(String UnknownTag) {
				WebElement element = driver.findElement(By.xpath(UnknownTag));
				return element;
			}

			// JavaScriptExecuter methods
			public WebElement SendKeys(String sendkey, String WebelementRef) {
				JavascriptExecutor js = (JavascriptExecutor) driver;
				WebElement element = driver.findElement(By.id(WebelementRef));
				js.executeScript(sendkey, element);
				return element;
			}

			public WebElement cliCk(String clickscript, String scriptvalue) {
				JavascriptExecutor js = (JavascriptExecutor) driver;
				WebElement element = driver.findElement(By.id(scriptvalue));
				js.executeScript(clickscript, element);
				return element;
			}

			public WebElement getParticularValueScript(String arguments, String getText) {
				JavascriptExecutor js = (JavascriptExecutor) driver;
				WebElement element = driver.findElement(By.xpath(getText));
				js.executeScript(getText, element);
				return element;
			}

			public WebElement scrollDown(String downpageSyntax, String textXpath) {
				JavascriptExecutor js = (JavascriptExecutor) driver;
				WebElement element = driver.findElement(By.xpath(textXpath));
				js.executeScript(downpageSyntax, element);
				return element;

			}

			public WebElement scrollUp(String uppageSyntax, String textXpath) {
				JavascriptExecutor js = (JavascriptExecutor) driver;
				WebElement element = driver.findElement(By.xpath(textXpath));
				js.executeScript(uppageSyntax, element);
				return element;
			}

			public void swtichWindow(String nameorHandles) {
				driver.switchTo().window(nameorHandles);

			}

			public String getParentWindowId(String windowhandle) {
				String windowHandle2 = driver.getWindowHandle();
				return windowHandle2;
			}

			public Set<String> getParentWindows() {
				Set<String> windowHandles = driver.getWindowHandles();
				return windowHandles;
			}

			// Action base class
			public void movetooElement(WebElement text) {
				act.moveToElement(text).perform();
			}

			public void doubleClick() {
				act.doubleClick().perform();
			}

			public void rightclick() {
				act.contextClick().perform();
			}

			public WebElement dragAndDrop(String source, String destiny) {
				WebElement element = driver.findElement(By.xpath(source));
				element.click();
				WebElement element2 = driver.findElement(By.xpath(destiny));
				act.dragAndDrop(element, element2).perform();
				return element;
			}

			// MoveToElement and keydown and keyup

			public void keyPressAndRelease(WebElement element) {
				act.moveToElement(element).keyDown(Keys.CONTROL).click().keyUp(Keys.CONTROL).perform();
			}

			public void keypress(WebElement element) {
				act.keyDown(element, Keys.CONTROL).click().perform();

			}

			public void keyrelease(WebElement element) {
				act.keyUp(element, Keys.CONTROL).perform();

			}

			public void keyPress() {
				act.keyDown(Keys.CONTROL).click().perform();

			}

			public void keyRelease() {
				act.keyUp(Keys.CONTROL).perform();

			}

			// Robot class
			public void keypress(int num) {
				rb.keyPress(num);

			}

			public void keyrelease(int num) {
				rb.keyRelease(num);
			}

			// Navigation methods

			public static void navigateToUrl(String url) {
				driver.navigate().to(url);
			}

			public static void navigateBack() {
				driver.navigate().back();
			}

			public static void navigateForward() {
				driver.navigate().forward();
			}

			public static void Refresh() {
				driver.navigate().refresh();
			}

			// Alert Interface
			// Simple Alert & confirm alert --Alert with ok Button and cancel button
			public void acceptAlert() {
				alert = driver.switchTo().alert();
				alert.accept();

			}

			public void dismissAlert() {
				alert.dismiss();
			}

			// Prompt alert -- Alert with text box and Ok button and Cancel Button
			public void getText() {
				String text = alert.getText();
				System.out.println(text);
			}

			public void alertSendkeys(String name) {
				alert.sendKeys(name);
			}

			// select class
			public void isMultiple(WebElement element) {
				Select s = new Select(element);
				boolean multiple = s.isMultiple();
				System.out.println(multiple);

			}

			public void selectByIndex(WebElement element, int num) {
				Select s = new Select(element);
				s.selectByIndex(num);
			}

			public void selectByValue(WebElement element, String value) {
				Select s = new Select(element);
				s.selectByValue(value);
			}

			public void selectByVisibleText(WebElement element, String text) {
				Select s = new Select(element);
				s.selectByVisibleText(text);

			}

			public void getAllSelectedOptions(WebElement element, String text) {
				Select s = new Select(element);
				List<WebElement> allSelectedOptions = s.getAllSelectedOptions();
				System.out.println(allSelectedOptions);
			}

			public void getFirstSelectedOptions(WebElement element, String text) {
				Select s = new Select(element);
				WebElement firstSelectedOption = s.getFirstSelectedOption();
				System.out.println(firstSelectedOption);
			}

			public void deSelectByValue(WebElement element, String value) {
				Select s = new Select(element);
				s.deselectByValue(value);

			}

			public void deSelectByIndex(WebElement element, int num) {
				Select s = new Select(element);
				s.deselectByIndex(num);
			}

			public void deSelectByVisibleText(WebElement element, String text) {
				Select s = new Select(element);
				s.deselectByVisibleText(text);
			}

			public void deSelectAll(WebElement element) {
				Select s = new Select(element);
				s.deselectAll();
			}

			public void getOptions(WebElement element) {
				Select s = new Select(element);
				WebElement wrappedElement = s.getWrappedElement();
				System.out.println(wrappedElement);
			}

			// Whole page screenshot
			public static File wholePage(String filename) throws IOException {

				File source = screenShot.getScreenshotAs(OutputType.FILE);
				File dest = new File("C:\\Users\\Herbert\\eclipse-workspace\\SeleniumProject\\LibraryFolder\\ScreenShot\\"
						+ filename + ".png");
				FileUtils.copyFile(source, dest);
				return source;
			}

			// take Particular image or text
			public static File particulatPlace(WebElement element, String filename) throws IOException {
				File source = element.getScreenshotAs(OutputType.FILE);
				File dest = new File("C:\\Users\\Herbert\\eclipse-workspace\\SeleniumProject\\LibraryFolder\\ScreenShot\\"
						+ filename + ".png");
				FileUtils.copyFile(source, dest);
				return source;
			}
		}





