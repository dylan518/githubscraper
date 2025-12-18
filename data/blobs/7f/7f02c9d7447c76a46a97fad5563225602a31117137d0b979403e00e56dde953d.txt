package com.ssafy.ssafit.model.dto;

import java.time.LocalTime;

import io.swagger.v3.oas.annotations.media.Schema;

@Schema(description = "운동 기록 DTO")
public class Exercise {
	private String userId;
	private String startTime;
	private String endTime;
	private String exerciseDate;
	private String exerciseKind;
	private int exerciseTime;

	public Exercise(String userId, String startTime, String endTime, String exerciseDate, String exerciseKind,
			int exerciseTime) {
		super();
		this.userId = userId;
		this.startTime = startTime;
		this.endTime = endTime;
		this.exerciseDate = exerciseDate;
		this.exerciseKind = exerciseKind;
		this.exerciseTime = exerciseTime;
	}

	public Exercise() {

	}

	public int getExerciseTime() {
		return exerciseTime;
	}

	public void setExerciseTime(int exerciseTime) {
		this.exerciseTime = exerciseTime;
	}

	public String getUserId() {
		return userId;
	}

	public void setUserId(String userId) {
		this.userId = userId;
	}

	public String getStartTime() {
		return startTime;
	}

	public void setStartTime(String startTime) {
		this.startTime = startTime;
	}

	public String getEndTime() {
		return endTime;
	}

	public void setEndTime(String endTime) {
		this.endTime = endTime;
	}

	public String getExerciseDate() {
		return exerciseDate;
	}

	public void setExerciseDate(String exerciseDate) {
		this.exerciseDate = exerciseDate;
	}

	public String getExerciseKind() {
		return exerciseKind;
	}

	public void setExerciseKind(String exerciseKind) {
		this.exerciseKind = exerciseKind;
	}

}
