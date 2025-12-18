package DesignPrinciples.DependencyInversionPrinciple;

// High Level Class

public class BudgetReport {
    private Database database; // Dependency is on the Abstraction (Database Interface)

    // Constructor Injection of the Database dependency
    public BudgetReport(Database database) {
        this.database = database;
    }

    public void open(String date) {
        System.out.println("Budget Report Opened for date: " + date);
        // Logic to fetch and process budget data, using database operations
    }

    public void save() {
        System.out.println("Budget Report Saving...");
        database.insert(); // Using the abstraction for database interaction
        database.update();
        database.delete();
        System.out.println("Budget Report Saved.");
    }
}