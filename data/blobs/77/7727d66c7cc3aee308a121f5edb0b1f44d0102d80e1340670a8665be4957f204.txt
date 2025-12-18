package com.atguigu.test1;

import java.util.Scanner;

public class TestStudent {
    public static void main(String[] args) {
//        Student stu = new Student();
//        stu.stuName = "Tom";
//        stu.score = 95;
//        stu.showInfo();

        Scanner input = new Scanner(System.in);
        Student[] stus = new Student[5];

        for (int i = 0; i < stus.length; i++) {
           stus[i] =  new Student();//为数组元素创建对象
            System.out.println("请输入学员姓名");
            stus[i].stuName = input.next();
            System.out.println("请输入学员分数");
            stus[i].score = input.nextInt();
            stus[i].showInfo();
        }
    }
}
