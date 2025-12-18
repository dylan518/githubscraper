package jumpstatement;

public class breakStatement {

	
	
	public static void main(String[] args) {
		
		
		int shop = 0;
		
		boolean paid=false;
		
		boolean unpaid=false;
		
		

		for (shop = 1; shop <= 6; shop++) {

			
			if (shop == 2) {

				paid=false;
				
                 break;
                 
			}
			
			System.out.println("Rent is  collected for shop "+shop);
		}
	}
}
