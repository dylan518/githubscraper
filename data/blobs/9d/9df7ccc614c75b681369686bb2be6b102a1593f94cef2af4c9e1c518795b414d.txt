package projectschoolmanagementsystem;
import java.io.Serializable;

/**
 * Represents a classroom in the school management system.
 * Implements {@link Serializable} to allow instances of this class to be serialized for file storage.
 * 
 * The class contains attributes for a unique classroom identifier and the maximum student capacity.
 * It provides getter and setter methods for both attributes, with validation for the capacity value.
 * 
 * @author Dieudonne
 */
public class Classroom implements Serializable {

    private static final long serialVersionUID = 1L; // Unique identifier for serialization
    
    private String classroomID; // Unique identifier for the classroom
    private int capacity; // Maximum number of students the classroom can accommodate

    /**
     * Constructs a Classroom object with the specified ID and capacity.
     * 
     * @param classroomID The unique identifier for the classroom.
     * @param capacity The maximum number of students the classroom can accommodate.
     */
    public Classroom(String classroomID, int capacity) {
        this.classroomID = classroomID;
        this.capacity = capacity;
    }

    /**
     * Gets the unique identifier of the classroom.
     * 
     * @return The classroom ID as a String.
     */
    public String getClassroomID() {
        return classroomID;
    }

    /**
     * Sets a new unique identifier for the classroom.
     * 
     * @param classroomID The new classroom ID to be set.
     */
    public void setClassroomID(String classroomID) {
        this.classroomID = classroomID;
    }

    /**
     * Gets the maximum student capacity of the classroom.
     * 
     * @return The capacity as an integer.
     */
    public int getCapacity() {
        return capacity;
    }

    /**
     * Sets the maximum student capacity for the classroom.
     * Ensures that the capacity value is greater than zero.
     * 
     * @param capacity The new capacity to be set.
     * @throws IllegalArgumentException If the capacity is less than or equal to zero.
     */
    public void setCapacity(int capacity) {
        if (capacity > 0) {
            this.capacity = capacity;
        } else {
            throw new IllegalArgumentException("Capacity must be greater than zero.");
        }
    }
}
