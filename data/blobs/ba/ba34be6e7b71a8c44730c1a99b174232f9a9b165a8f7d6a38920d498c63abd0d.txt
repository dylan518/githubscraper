package designingpatterns;

public class Employee {
		private  static Employee instance = null;
		
		private Employee() {
			System.out.println("Employee Object is Created");
			
		}
		public static Employee getinstance() {
			if(instance == null) {
				instance = new Employee();
			}
			return instance;
			
		}
		
	 public void EmployeeId() {
		 System.out.println("EmployeeId 52159........");
	 }
	 
	}



