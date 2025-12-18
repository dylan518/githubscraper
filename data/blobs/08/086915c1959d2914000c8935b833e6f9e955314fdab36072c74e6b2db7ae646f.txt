package org.step;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import net.masterthought.cucumber.Configuration;
import net.masterthought.cucumber.ReportBuilder;




public class JVMReportSample {

	public static void reportGenerate (String JsonPath) {
		
		//1. mention location
		File f = new File(System.getProperty("user.dir")+"\\AllReports\\JVM Reports");
		
		//2.Configuration object creations
		Configuration c = new Configuration(f,"Facebook Applicvation");
		c.addClassifications("Windows", "10");
		c.addClassifications("JDK", "11");
		c.addClassifications("Sprint", "15");
		c.addClassifications("Testers", "4");
		
		//3.add the List file to generate reports
		
		List<String> li = new ArrayList();
		li.add(JsonPath);
		
		//4.report generate
		ReportBuilder r = new ReportBuilder(li, c);
		r.generateReports();
		
		
		
		
		
		
		
		
		
		
	}
	
	
	
	
	
	
	
	
}
