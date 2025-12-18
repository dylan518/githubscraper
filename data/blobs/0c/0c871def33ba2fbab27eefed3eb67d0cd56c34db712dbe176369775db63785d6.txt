package com.bridgelabz.qa.Automation;

import java.util.List;
import java.util.Map;
import java.util.Set;

import org.testng.IReporter;
import org.testng.ISuite;
import org.testng.ISuiteResult;
import org.testng.ITestContext;
import org.testng.ITestResult;
import org.testng.xml.XmlSuite;

public class ReporterListener implements IReporter {

	@Override
	public void generateReport(List<XmlSuite> xmlSuites, List<ISuite> suites, String outputDirectory) {
		for(ISuite suite : suites) {
			String suiteName = suite.getName();
			
			Map<String, ISuiteResult>suiteResults = suite.getResults(); 
			for(ISuiteResult sr : suiteResults.values()) {
				ITestContext tc = sr.getTestContext();
				System.out.println("Passed test for suites = "+suiteName+ "is"+tc.getPassedTests().getAllResults().size());
				System.out.println("Failed test for suites = "+suiteName+ "is"+tc.getFailedTests().getAllResults().size());
				System.out.println("Skipped test for suites = "+suiteName+ "is"+tc.getSkippedTests().getAllResults().size());
				
				Set<ITestResult> passesTestResults = tc.getPassedTests().getAllResults();
				
				for (ITestResult passesTestResult : passesTestResults) {
					String methodName = passesTestResult.getName();
					System.out.println("Method Name : "+ methodName);
					System.out.println("Status :"+ passesTestResult.getThrowable());
				}
			}
		}
	}
}
