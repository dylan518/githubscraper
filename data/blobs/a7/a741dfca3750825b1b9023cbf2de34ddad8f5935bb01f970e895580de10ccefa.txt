package actionpage.onlineshop;


import locatorpage.onlineshop.HomepageLocator;
import utility_onlineshop.Onlineshop_Base;

public class HomePageAction extends Onlineshop_Base   {
	
	HomepageLocator homepageLocator= new HomepageLocator();
	
	public void Click_account_link() {
		homepageLocator.Accountlink.click();
		
	}
	
	
	
}
