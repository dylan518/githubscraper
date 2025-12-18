package com.logger.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.logger.dao.Taskdao;
import com.logger.entities.TaskDetailsMaster;

@Service
public class TaskService {
	
	@Autowired
	Taskdao dao;

	public int  addtask(TaskDetailsMaster task) {
		return dao.createtask(task);
	}
	
	public List<TaskDetailsMaster> getAllTasksByTaskDate(String d1,String d2){
		return dao.getAllTasksByDate(d1,d2);
	}
	
	public List<TaskDetailsMaster> getAllTasksByDateAndProject(String d1,String d2,String projectid){
		return dao.getAllTasksByDateAndProject(d1,d2,projectid);
	}
	
	public List<TaskDetailsMaster> getTasksByDateAndPerson(String d1,String d2,String piid){
		return dao.getAllTasksByDateAndPerson(d1, d2, piid);
	}
	
	public List<TaskDetailsMaster> getTasksByAllParams(String d1,String d2,String piid,String projid){
		return dao.getAllTasksByAll(d1, d2, piid, projid);
	}
	
}
