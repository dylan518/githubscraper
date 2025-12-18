package utils.listeners;

import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;
import utils.logger.ILogger;

public class RetryAnalyzer implements IRetryAnalyzer, ILogger {
    private int retryCount = 0;
    private int maxRetryCount ;
    private static boolean isRerun = false;


    public boolean retry(ITestResult result) {
        if (retryCount < getMaxRetryCount()) {
            LOG.info("Retrying Test " + result.getName() + " with status "
                    + getResultStatusName(result.getStatus()) + " for the " + (retryCount + 1) + " time(s).");
            result.setStatus(ITestResult.FAILURE);

            retryCount++;
            isRerun = true;
            return true;
        }
        else{
            retryCount = 0;
            isRerun = false;
        }

        return false;
    }

    public String getResultStatusName(int status) {
        String resultName = null;
        if (status == 1) {
            resultName = "SUCCESS";
        }
        if (status == 2) {
            resultName = "FAILURE";
        }
        if (status == 3)
            resultName = "SKIP";
        return resultName;
    }

    public boolean isRerun() {
        return isRerun;
    }
    public boolean isRetryAvailable() {
        return retryCount < getMaxRetryCount();
    }
    public boolean isRetryAvailableForValidateSkipTest() {
        return retryCount <= getMaxRetryCount();
    }

    public int getMaxRetryCount(){
        if(System.getenv("MAX_RETRY_COUNT")!=null){
            maxRetryCount=Integer.parseInt(System.getenv("MAX_RETRY_COUNT"));
        }
        else{
            maxRetryCount=2;
        }
        return maxRetryCount;
    }
}
