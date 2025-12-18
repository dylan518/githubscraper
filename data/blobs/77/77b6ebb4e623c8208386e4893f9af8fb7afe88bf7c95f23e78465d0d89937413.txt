package com.comrade.java_8.collectors.toSet;

import com.comrade.utils.StreamUtil;
import com.comrade.utils.Student;

import java.util.List;
import java.util.stream.Collectors;

public class CollectorsToSetClient {
    public static void main(String[] args) {
        List<Student> students = StreamUtil.studentsBuilder();
        var firstName = students.stream().map(Student::getFirstName).collect(Collectors.toSet());
        var lastName = students.stream().map(Student::getLastName).collect(Collectors.toSet());
        System.out.println(firstName);
        System.out.println(lastName);
    }
}
