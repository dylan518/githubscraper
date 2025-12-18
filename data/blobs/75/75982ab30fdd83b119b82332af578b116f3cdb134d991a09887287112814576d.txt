package com.bestbuy.tests;

import org.testng.annotations.Test;

import com.bestbuy.utils.SeWrappers;
import com.bestbuy.utils.bestbuyWrappers;

public class ProductPageTest  extends SeWrappers{
	   bestbuyWrappers bb= new bestbuyWrappers();
		SeWrappers se= new SeWrappers();
		@Test
		public void AddProduct() throws InterruptedException
		{
			launchBrowser("https://www.bestbuy.com/");
			//bb.Loginpage("maniblaze81@gmail.com", "Mani231297@");
			bb.ProductPg("laptop");
		}

}
