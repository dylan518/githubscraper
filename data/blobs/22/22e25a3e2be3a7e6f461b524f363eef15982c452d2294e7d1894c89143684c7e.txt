package employeestreamproblems;

import java.util.List;

public class NAmeOfAllOrganization {

	public static void main(String[] args) {
		List<Employee> employes = EmployeeDB.findAll();
		
		employes.stream()
		     .map(Employee :: getDepartment)
		     .distinct()
		     .forEach(System.out::println);
	}
}
