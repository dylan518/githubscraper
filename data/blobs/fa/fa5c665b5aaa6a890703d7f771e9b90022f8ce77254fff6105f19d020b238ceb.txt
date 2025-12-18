package utilities;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.reporter.ExtentHtmlReporter;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.apache.commons.io.FileUtils;
import org.junit.After;
import org.junit.Before;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.awt.*;
import java.awt.datatransfer.StringSelection;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Date;

public abstract class TestBase {
    //abstract class yaptik cunku obje olusturulmasini istemiyoruz , depo olarak kullanacagiz.
    //Bu class'a extend ettigimiz test class'larindan ulasabiliriz.
    //TestBase class'indan obje olusturulmasinin onune gecilmesi icin abstract class yapilabilir.

    protected ExtentReports extentReports; // --> Raporlamayi baslatmak icin kullanilan class
    protected ExtentHtmlReporter extentHtmlReporter;// -->Raporu HTML formatinda duzenler
    protected ExtentTest extentTest;// --> Test adimlarina eklemek istedigimiz bilgileri bu class ile olustururuz.

    protected WebDriver driver;
    //olusturudugumuz driver'i kullanabilmemiz icin protected yaptik.

    @Before
    public void setUp() throws Exception {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(15));
    }

    @After
    public void tearDown() throws Exception {
        extentReports = new ExtentReports();
        extentReports.flush();
       // driver.quit();
    }

    public void wait(int seconds) {

        try {
            Thread.sleep(seconds * 1000);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

    //visibilityOf(element) methodu
    public void visibileWait(WebElement element, int saniye) {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(saniye));
        wait.until(ExpectedConditions.visibilityOf(element));
    }

    //visibilityOf(locator) methodu
    public void visibileWait(By locator, int saniye) {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(saniye));
        wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
    }

    //alertWait
    public void alertWait(int saniye) {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(saniye));
        wait.until(ExpectedConditions.alertIsPresent());
    }

    //FluentWait visible method
    public void fluentWaitVisible(WebElement element, int saniye, int salise) {
        new FluentWait<>(driver).withTimeout(Duration.ofSeconds(saniye)).
                pollingEvery(Duration.ofMillis(salise)).
                until(ExpectedConditions.visibilityOf(element));
    }

    public void alertAccept() {
        driver.switchTo().alert().accept();
    }

    public void alertDismiss() {
        driver.switchTo().alert().dismiss();
    }

    public void alertPrompt(String text) {
        driver.switchTo().alert().sendKeys(text);
    }

    public void alertText() {
        System.out.println(driver.switchTo().alert().getText());
    }

    public void ddmVisibleText(WebElement ddm, String secenek) {
        Select select = new Select(ddm);
        select.selectByVisibleText(secenek);
    }

    public void ddmIndex(WebElement ddm, int index) {
        Select select = new Select(ddm);
        select.selectByIndex(index);
    }

    public void ddmValue(WebElement ddm, String value) {
        Select select = new Select(ddm);
        select.selectByValue(value);
    }

    //ScreenShot
    public void takeScreenShot() {
        String date = new SimpleDateFormat("_hh_mm_ss_ddMMyyyy").format(new Date()); // tarihle ilgili yeni bir format
        TakesScreenshot ts = (TakesScreenshot) driver;
        try {
            FileUtils.copyFile(ts.getScreenshotAs(OutputType.FILE), new File("Screenshot/screenShot" + date + ".png"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    //webElement screenshot
    public void webElementScreenshot(WebElement webElement) {
        String date = new SimpleDateFormat("_hh_mm_ss_ddMMyyyy").format(new Date()); // tarihle ilgili yeni bir format
        //  String dosyaYolu = "src/test/java/techproed/WebElementScreenShot//WEscreenShot" + date + ".jpeg";
        String dosyaYolu = "src/test/java/techproed/WebElementPictures/WEscreenShot" + date + ".jpeg";
        try {
            FileUtils.copyFile(webElement.getScreenshotAs(OutputType.FILE), new File(dosyaYolu));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    //SwitchTo Window-2
    public void switchToWindow2(int index) {
        driver.switchTo().window(driver.getWindowHandles().toArray()[index].toString());
    }

    //UploadFile Robot Class
    public void uploadFilePath(String filePath) {
        try {
            wait(3);
            StringSelection stringSelection = new StringSelection(filePath);
            Toolkit.getDefaultToolkit().getSystemClipboard().setContents(stringSelection, null);
            Robot robot = new Robot();
            robot.keyPress(KeyEvent.VK_CONTROL);
            wait(3);
            robot.keyPress(KeyEvent.VK_V);
            wait(3);
            robot.keyRelease(KeyEvent.VK_CONTROL);
            wait(3);
            robot.keyRelease(KeyEvent.VK_V);
            wait(3);
            robot.keyPress(KeyEvent.VK_ENTER);
            wait(3);
            robot.keyRelease(KeyEvent.VK_ENTER);
            wait(3);
        } catch (AWTException e) {
            throw new RuntimeException(e);
        }
    }


    //Extent Report Methodu
    public void extentReport(String browser, String reportName) {
        extentReports = new ExtentReports();
        String date = new SimpleDateFormat("_hh_mm_ss_ddMMyyyy").format(new Date()); // tarihle ilgili yeni bir format
        String dosyaYolu = "testOutput/extentReports/extentReport" + date + ".html";
        extentHtmlReporter = new ExtentHtmlReporter(dosyaYolu);
        extentReports.attachReporter(extentHtmlReporter);//-->HTML formatinda raporlamayi baslatacak.

        //Rapor da gozukmesini istedigimiz bilgiler icin
        extentReports.setSystemInfo("Browser", browser);
        extentReports.setSystemInfo("Tester", "Omer");
        extentHtmlReporter.config().setDocumentTitle("Extent Report");
        extentHtmlReporter.config().setReportName(reportName);

        //  extentTest = extentReports.createTest(testName, description);

    }

    public void scroll(WebElement element){

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].scrollIntoView(true);",element);

    }

    public void scrollHome(){

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollTo(0, -document.body.scrollHeight);");

    }

    public void scrollEnd(){

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("window.scrollTo(0, document.body.scrollHeight);");

    }

    public void sendKeysJS(WebElement element ,String test){

        JavascriptExecutor js= (JavascriptExecutor) driver;
        js.executeScript("arguments[0].value='"+test+"'",element);
    }

    public void sendAttributeJS(WebElement element, String text){

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].setAttribute('value','"+text+"')",element);
    }

}
