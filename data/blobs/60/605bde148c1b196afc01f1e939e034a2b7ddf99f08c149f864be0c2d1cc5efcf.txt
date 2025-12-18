package com.controller;

import com.repository.EmployeeRepository;
import com.repository.NotificationRepository;
import com.service.EmployeeService;
import com.service.NotificationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/dashboard")
public class DashboardController {

    @Autowired
    private NotificationService notificationService;

    @Autowired
    private EmployeeService employeeService;

    @Autowired
    private NotificationRepository notificationRepository;

    @Autowired
    private EmployeeRepository employeeRepository;

    @GetMapping("/dashboard")
    public String dashboard(Model model) {
        // Get total employee count from service
        long employeeCount = employeeService.getEmployeeCount();

        // Get total notification count from repository (Ensure this method is correct)
        long notificationCount = notificationRepository.count(); // You can also use notificationService



        System.out.println("Employee Count: " + employeeCount);
        System.out.println("Notification Count: " + notificationCount);
        // Add both counts to the model to pass to the view
        model.addAttribute("employeeCount", employeeCount);
        model.addAttribute("newNotifications", notificationCount); // For "New Notifications"

        // Return the index.html view (the dashboard page)
        return "index";  // Ensure this matches the view file name
    }
}
