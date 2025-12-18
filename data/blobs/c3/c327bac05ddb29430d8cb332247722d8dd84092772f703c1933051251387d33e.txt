// October 24, 2023
/* This program creates an enum class called TrafficLight which has constants RED, GREEN, YELLOW each taking 1 parameter
 * which is the duration of each light. A program is created to test the TrafficLight enum class and print out the constants
 * along with their time duration
 */
package chapter08HW;

public enum TrafficLight {
	// Create the constants containing one parameter which is the time duration
	GREEN(60),
	YELLOW(10),
	RED(35);
	
	// The "time" variable will hold the value of the parameter of the enum constant which will also be constant
	private final int time;
	
	// Create a constructor to initialize the time when an object is created
	TrafficLight(int time) {
		this.time = time;
	}
	
	// Create an accessor method to return the time
	public int getTime() {
		return time;
	}
}
