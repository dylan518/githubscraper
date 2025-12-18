package com.LIMS.Retry;

import org.testng.IRetryAnalyzer;

import org.testng.ITestResult;
/**
 * 
 * @author kishore mallarapu
 *
 */
public class RetryImplementation implements IRetryAnalyzer {
	int count;

	@Override
	public boolean retry(ITestResult result) {
		int maxCount = 3;
		if (count < maxCount) {
			count++;
			return true;

		}

		return false;
	}

}
