package tek.week_9.day_3;

import java.util.LinkedList;

public class VehicleManager {
	
	// Create a class called VehicleManager
	// Create an LinkedList
	LinkedList<String> vehicles;
	// Create a constructor that is going to initialize the linkedList
	public VehicleManager() {
		vehicles = new LinkedList<>();
	}
	// Create methods of your choice to perform custom operations like add or
	// delete.
	
	void addVehicle(String name) {
		vehicles.add(name);
	}
	
	void removeVehicle(String name) {
		vehicles.remove(name);
	}
	
	void printVehicles() {
		System.out.println("List of available vehicles:");
		for (String v : vehicles) {
			System.out.println(v);
		}
	}
}