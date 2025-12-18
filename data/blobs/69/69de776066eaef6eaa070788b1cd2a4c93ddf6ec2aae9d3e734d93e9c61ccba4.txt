
// all the project done by me Hassan, 28-10-2024, except main by GPT
package com.managment.tasks;

import java.time.LocalDate;
import java.util.Scanner;

public class MainClass {

    public static void main(String[] args) {
        TaskManager taskManager = new TaskManager();
        Scanner scanner = new Scanner(System.in);

        // Load existing tasks from file, if any
        
        boolean  loadStatus = taskManager.loadTasks();
            if (loadStatus)
            {
            	System.out.println("Tasks loaded from file successfully.");
            }
            else {
                System.out.println("No saved tasks found or error loading tasks ");

            }
       
        

        boolean running = true;
        while (running) {
            displayMainMenu();

            System.out.print("\nYour choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (choice) {
                case 1 -> addTask(taskManager, scanner);
                case 2 -> editTask(taskManager, scanner);
                case 3 -> completeTask(taskManager, scanner);
                case 4 -> viewTasks(taskManager);
                case 5 -> sortTasksByPriority(taskManager);
                case 6 -> sortTasksByDueDate(taskManager);
                case 7 -> {
                    saveData(taskManager);
                    running = false;
                }
                default -> System.out.println("Invalid option! Please select a valid choice.");
            }
        }
        scanner.close();
    }

    // Method to display the main menu with styling
    private static void displayMainMenu() {
        System.out.println("\n===================================");
        System.out.println("        Task Management System      ");
        System.out.println("===================================");
        System.out.println("1. Add Task");
        System.out.println("2. Edit Task");
        System.out.println("3. Complete Task");
        System.out.println("4. View Tasks");
        System.out.println("5. Sort Tasks by Priority");
        System.out.println("6. Sort Tasks by Due Date");
        System.out.println("7. Save and Exit");
        System.out.println("===================================");
    }

    private static void addTask(TaskManager taskManager, Scanner scanner) {
        System.out.println("\n--- Add New Task ---");
        System.out.print("Enter Task Title: ");
        String title = scanner.nextLine();
        System.out.print("Enter Task Description: ");
        String description = scanner.nextLine();
        System.out.print("Enter Priority (HIGH, MEDIUM, LOW): ");
        String priorityInput = scanner.nextLine().toUpperCase();
        Priority priority = Priority.valueOf(priorityInput);  // Assuming Priority is an enum
        System.out.print("Enter Due Date (YYYY-MM-DD): ");
        LocalDate dueDate = LocalDate.parse(scanner.nextLine());
        System.out.print("Enter Status (PENDING, COMPLETED): ");
        String statusInput = scanner.nextLine().toUpperCase();
        TaskStatus status = TaskStatus.valueOf(statusInput);  // Assuming TaskStatus is an enum

        Task task = new Task(title, description, dueDate, status ,priority);
        taskManager.addTask(task);
        System.out.println("\nTask added successfully!\n");
    }

    private static void editTask(TaskManager taskManager, Scanner scanner) {
        System.out.println("\n--- Edit Task ---");
        System.out.print("Enter the Title of the Task to Edit: ");
        String title = scanner.nextLine();
        
        System.out.println("Enter updated task details:");
        addTask(taskManager, scanner);  // Can reuse addTask() to update the existing task
    }

    private static void completeTask(TaskManager taskManager, Scanner scanner) {
        System.out.println("\n--- Complete Task ---");
        System.out.print("Enter the Title of the Task to Complete: ");
        String title = scanner.nextLine();
        if( taskManager.completeTask(title))
        {
        System.out.println("\nTask done successfully!\n");
        }
        }

    private static void viewTasks(TaskManager taskManager) {
        System.out.println("\n--- List of All Tasks ---");
        System.out.println("===================================");
        
        for (Task task :taskManager.viewTasks())
        {
        	System.out.println("Task :"+task.toString());
		
        }
        
        System.out.println("===================================\n");
    }

    private static void sortTasksByPriority(TaskManager taskManager) {
        System.out.println("\n--- Tasks Sorted by Priority ---");
        //taskManager.sortTasksByPriority();
        taskManager.viewTasks();
    }

    private static void sortTasksByDueDate(TaskManager taskManager) {
        System.out.println("\n--- Tasks Sorted by Due Date ---");
        //taskManager.sortTasksByDueDate();
        taskManager.viewTasks();
    }

    private static void saveData(TaskManager taskManager) {
        try {
            taskManager.saveTasks();
            System.out.println("Tasks saved to file successfully.");
        } catch (Exception e) {
            System.out.println("Error saving tasks to file: " + e.getMessage());
        }
    }
}
