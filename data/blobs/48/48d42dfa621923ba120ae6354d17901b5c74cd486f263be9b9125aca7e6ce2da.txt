package com.fsh.lecturesystem.dto;

import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CourseEnrolledUserDTO {
    private Long userId;
    private Long courseId;

    public CourseEnrolledUserDTO(Long userId, Long courseId) {
        this.userId = userId;
        this.courseId = courseId;
    }
}
