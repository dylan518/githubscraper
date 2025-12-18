package manager;

import com.google.common.io.Files;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class TakeScreenShot {
    static Logger logger = LoggerFactory.getLogger(TakeScreenShot.class);

    public static void main(String[] args) {
        System.out.println(createFileNameScreenShot());
    }

    public static void takeScreenShot(TakesScreenshot screenshot) {
        String fileName = createFileNameScreenShot();
        File scrFile = screenshot.getScreenshotAs(OutputType.FILE);
        try {
            Files.copy(scrFile, new File(fileName));
            logger.info("create screenshot with file name --> " + fileName);
        } catch (IOException e) {
            logger.error("create exception in method takeScreenShot -->"+e.toString());
            throw new RuntimeException(e);

        }
    }

    private static String createFileNameScreenShot() {
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd_HH-mm-ss");
        Date date = new Date(System.currentTimeMillis());
        System.out.println(date);
        String currentDate = formatter.format(date);
        System.out.println(currentDate);
        String filePath = "logs/screenshots/screenshot_" + currentDate + ".png";
        return filePath;
    }




//    public static void takeScreenShot1(TakesScreenshot takesScreenshot){
//        File srcFile = takesScreenshot.getScreenshotAs(OutputType.FILE);
//        try {
//            Files.copy(srcFile,new File(createNameScreenShot1()));
//        } catch (IOException e) {
//            throw new RuntimeException(e);
//        }
//    }
//
//    private static String createNameScreenShot1() {
//        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd_HH-mm-ss");
//        Date date = new Date(System.currentTimeMillis());
//        String currentDate =  formatter.format(date);
//        String filePath = "logs/screenshots/screenshot"+currentDate+".png";
//        return filePath;
//    }

//    public static void takeScreenShot1(TakesScreenshot takesScreenshot){
//        File srcFile = takesScreenshot.getScreenshotAs(OutputType.FILE);
//        try {
//            Files.copy(srcFile,new File(createFileNameScreenShot1()));
//        } catch (IOException e) {
//            throw new RuntimeException(e);
//        }
//    }
//
//    private static String createFileNameScreenShot1() {
//        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd_HH-mm-ss");
//        Date date = new Date(System.currentTimeMillis());
//        String currentDate  = formatter.format(date);
//        String filePath = "logs/screenshots/screenshot"+currentDate+".png";
//        return filePath;
//    }
}