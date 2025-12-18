package com.indus.training.core.impl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.indus.training.core.entity.Student;
import com.indus.training.core.svc.IConverter;

public class JsonConverterUsingJackson implements IConverter {

	private final ObjectMapper objectMapper;

	public JsonConverterUsingJackson(ObjectMapper objectMapper) {
		this.objectMapper = objectMapper;
	}

	@Override
	public String convertToFormat(Student student) {
		try {
			return objectMapper.writeValueAsString(student);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public Student convertToJava(String jsonString) {
		try {
			return objectMapper.readValue(jsonString, Student.class);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
			return null;
		}
	}
}
