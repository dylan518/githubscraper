package com.quizapplication.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.quizapplication.model.Question;
import com.quizapplication.service.QuestionInf;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/question")
public class QuestionController {

	@Autowired
	@Qualifier("questionService")
	QuestionInf quizservice;
	
	@GetMapping("/allQuestion")
	public List<Question> allQuestion() {
		return quizservice.getallQuestion();
	}
	 
	@GetMapping("/fetchCategory/{category}")
	public List<Question> getCategory(@PathVariable String category){
		return quizservice.getDataCategory(category);
	}
	
	@GetMapping("/fetchId/{id}")
	public Question getById(@PathVariable int id){
		return quizservice.getById(id);
	}
	
	@GetMapping("/fetchDifficult/{difficultLevel}")
	public List<Question> getLevel(@PathVariable String difficultLevel){
		return quizservice.getDifficultLevel(difficultLevel);
	}
	
	@PostMapping("/saveQuestion")
	public String saveQue(@RequestBody @Valid Question question) {
		return quizservice.saveQuestion(question);
	}
	
	@PutMapping("/update")
	public Question update(@RequestBody @Valid Question que) {
		return quizservice.update(que);
	}
	
	@DeleteMapping("/delete/{id}")
	public String deleteid(@PathVariable int id) {
		return quizservice.deleteById(id);
	}
	
	
	@GetMapping("/fetchCD/{category}/{difficultLevel}")
	
	public List<Question> getCatDif(@PathVariable String category , @PathVariable String difficultLevel){
		return quizservice.getByCategoryAndDifficultLevel(category,difficultLevel);
	}
	
}
