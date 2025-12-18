package com.ILab1.controller;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.ILab1.entity.Marks;
import com.ILab1.entity.Subject;
import com.ILab1.services.MarksServices;
import com.ILab1.services.SubjectServices;

@Controller
public class MarksController {
	
	@Autowired
	SubjectServices subSer;
	@Autowired
	MarksServices markSer;
	
	@PostMapping("/addMarks")
	public String addMarks(@RequestParam ("marksId") int marksId,
			@RequestParam ("subjectId") int subjectId,
			@RequestParam ("marks") float marks)
	{
		try {
	
		Subject sub=subSer.getSubject(subjectId);
		Marks mark=new Marks(marksId, sub, marks);
		markSer.addMarksdata(mark);
		return "Sucessfull";
	}catch(Exception er)
	{
		return "Error";
	}
	}
	@GetMapping("/showMarks")
	public String showMarks(Model model)
	{
		try {
	
		List<Marks> clist=markSer.showAllMarks();
		model.addAttribute("MarksList", clist);
		return "ShowMarks";
	}catch(Exception er)
	{
		return "Error";
	}
	}
	@PostMapping("/updateMarks")
	public String updateMarks(@RequestParam ("MarksId") int MarksId,
			@RequestParam ("marks") float marks)
	{
		try {
		boolean has=markSer.hasId(MarksId);
		if(has==true)
		{
			Marks upmarks=markSer.getMarks(MarksId);
			upmarks.setMarks(marks);
			markSer.addMarksdata(upmarks);
		}
		return "Sucessfull";
		}catch(Exception er)
		{
			return "Error";
		}
	}
	@PostMapping("/deleteMarks")
	public String deleteMarks(@RequestParam ("MarksId") int MarksId)
	{
		try {
		boolean has=markSer.hasId(MarksId);
		if(has==true)
		{
			Marks upmarks=markSer.getMarks(MarksId);
			markSer.deleteMarksdata(upmarks);
		}
		return "Sucessfull";
	}catch(Exception er)
	{
		return "Error";
	}
	}
}
