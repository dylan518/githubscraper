package com.example.demo.controller;

import com.example.demo.entities.Task;
import com.example.demo.services.TaskServices;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.view.RedirectView;

import java.util.List;

@RestController
public class TaskController {

    private final TaskServices SERVICES;

    public TaskController(TaskServices services){
        this.SERVICES = services;
    }

/*
    @GetMapping("/tasks")
    public List<Task> getTaskList(){
        return SERVICES.getTaskList();
    }

 */

    @PostMapping("/tasks")
    public RedirectView createTask(@ModelAttribute @DateTimeFormat(pattern = "YYYY-MM-DD") Task task, Model model){
        model.addAttribute(task);
        task.setDone(false);
        this.SERVICES.createTask(task);
        return new RedirectView("/tasks");
    }

    @PatchMapping("/tasks/{id}")
    public RedirectView updateTask(@PathVariable("id") long id) {
        this.SERVICES.markTaskAsFinished(id);
        return new RedirectView("/tasks");
    }

    @DeleteMapping("/tasks/{id}")
    public RedirectView deleteTask(@PathVariable("id") long id){
        this.SERVICES.deleteTask(id);
        return new RedirectView("/tasks");
    }
}