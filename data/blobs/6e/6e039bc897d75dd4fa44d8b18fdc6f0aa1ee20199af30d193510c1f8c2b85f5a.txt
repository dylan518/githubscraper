package com.app.auth.exception;

import com.app.auth.dto.ApiError;
import com.app.auth.util.Constants;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.time.LocalDateTime;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ApiError> handlerGenericException(Exception exception, HttpServletRequest request) {

        ApiError error = new ApiError();
        error.setMessage(Constants.ERROR_PLEASE_TRY_AGAIN);
        error.setInternalMessage(exception.getLocalizedMessage());
        error.setTime(LocalDateTime.now());
        error.setHttpCode(500);

        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ApiError> handlerMethodArgumentNotValidException(MethodArgumentNotValidException exception, HttpServletRequest request) {

        ApiError error = new ApiError();
        error.setMessage(Constants.REQUEST_CHECK_THE_FORMAT);
        error.setInternalMessage(exception.getLocalizedMessage());
        error.setTime(LocalDateTime.now());
        error.setHttpCode(400);

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
    }

}
