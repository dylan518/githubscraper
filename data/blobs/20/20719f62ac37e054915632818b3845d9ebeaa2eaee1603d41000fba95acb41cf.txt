package StepG;

import java.util.Scanner;

public class G03Sub {

    // count 수 만큼의 학생 별 국/영/수 성적 입력 받아 저장하는 메소드
    public int[][] getScore(int[][] jumsu, int count) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < count; i++) {
            System.out.printf("Enter Korean, English, Math score of %dth student > ", i + 1);
            jumsu[i][0] = sc.nextInt();
            jumsu[i][1] = sc.nextInt();
            jumsu[i][2] = sc.nextInt();
        }
        sc.close();

        return jumsu;
    }

    // 각 과목별 총점과 평균 점수 출력하는 메소드
    public void printSubject(int[][] jumsu) {
        System.out.println("1) Total score and average for each subjects");
        int[] c_average = new int[3]; // 3과목 총점을 저장하고 있는 중복 리스트
        // int[] c_average = { 0, 0, 0 }; // 3과목 총점을 저장하고 있는 중복 리스트
        String[] class_name = { "Korean", "English", "Math" }; // 과목명 리스트

        for (int i = 0; i < jumsu.length; i++) {
            c_average[0] += jumsu[i][0];
            c_average[1] += jumsu[i][1];
            c_average[2] += jumsu[i][2];
        }

        for (int i = 0; i < 3; i++) {
            System.out.printf("Total %s score is %d, average is %.1f\n", class_name[i], c_average[i],
                    (double) c_average[i] / 5);
        }

    }

    // 각 학생별 총점과 평균점수, 평균에 따른 등급 출력하는 메소드
    public void printStudent(int[][] jumsu) {
        System.out.println("2) Total score and average for each students");
        // 총점, 평균, 등급 계산을 위한 변수
        int sum = 0;
        double average = 0;
        String grade;

        for (int i = 0; i < jumsu.length; i++) {
            sum = jumsu[i][0] + jumsu[i][1] + jumsu[i][2];
            average = (double) sum / 3;
            grade = checkGrade(average);
            System.out.printf("%dth student score: Total - %d, average - %.1f, grade - %s\n", i + 1, sum, average,
                    grade);
        }
    }

    // 등급을 계산해주는 메소드
    public String checkGrade(double average) {
        String grade = "";
        if (average >= 90) {
            grade = "A";
        } else if (average >= 80) {
            grade = "B";
        } else if (average >= 70) {
            grade = "C";
        } else if (average >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }
        return grade;
    }
}
