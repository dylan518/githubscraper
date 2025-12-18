package com.solutions.a3z.errors;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class EmployeeRestExceptionHandler {
	
    // add an exception handler using @ExceptionHandler
    @ExceptionHandler
    public ResponseEntity<EmployeeErrorResponse> handleException(EmployeeNotFoundException exc){
    	
    	//Create StudentErrorResponse
    	EmployeeErrorResponse stdError = new EmployeeErrorResponse();
    	stdError.setStatus(HttpStatus.NOT_FOUND.toString());
    	stdError.setMessage(exc.getMessage());
    	stdError.setTimeStamp(System.currentTimeMillis());
    	
    	//Return Response Entity
    	
		return new ResponseEntity<EmployeeErrorResponse>(stdError, HttpStatus.NOT_FOUND);
    }
    
    // add exception handler for generic exception
    @ExceptionHandler
    public ResponseEntity<EmployeeErrorResponse> handleException(Exception exc){
    	
    	EmployeeErrorResponse errorResponse = new EmployeeErrorResponse();
    	errorResponse.setStatus(HttpStatus.BAD_REQUEST.toString());
    	errorResponse.setMessage(exc.getMessage());
    	errorResponse.setTimeStamp(System.currentTimeMillis());
    	
    	return new ResponseEntity<EmployeeErrorResponse> (errorResponse, HttpStatus.BAD_REQUEST);
    }
	

}
