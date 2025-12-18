package com.guanhf.a12jdbc;

import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;

import static java.lang.System.exit;

/**
 * 功能:
 * 作者:
 * 日期:2024/10/18 8:47
 */
public class App {
    public static final Scanner sc = new Scanner(System.in);
    public static void main(String[] args) throws SQLException {
        while(true) {
            String username = login();
            if (username!=null) {
                program(username);
                System.out.println("login success!!!");
                break;
            }else {
                System.out.println("username or password is incorrect!!!");
            }
        }
    }

    // 分支执行
    public static void program(String username) throws SQLException {
        while (true) {
            int choice = menu(username);
            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    queryStudent();
                    break;
                case 3:
                    modifyStudent();
                    break;
                case 4:
                    deleteStudent();
                    break;
                case 5:
                    statisticsStudent();
                    break;
                case 6:
                    modifyPassword(username);
                    break;
                case 7:
                    System.out.println("exit successfully");
                    exit(0);
                    break;
                default:
                    System.out.println("invalid choice");

            }
        }
    }

    // 建立连接
    public static Connection getConnection() throws SQLException {
        String url = "jdbc:mysql://47.121.181.198:3307/java";
        String username = "root";
        String password = "123456";
        return DriverManager.getConnection(url, username, password);
    }

    // 用户登陆
    public static String  login() throws SQLException {
        Connection connection = getConnection();
        System.out.println("please enter your username: ");
        String username = sc.nextLine();
        System.out.println("please enter your password: ");
        String password = sc.nextLine();

        // 验证用户
        String sql = "select * from user where username = ? and password = ?";
        PreparedStatement ps = connection.prepareStatement(sql);
        ps.setString(1, username);
        ps.setString(2, password);
        ResultSet rs = ps.executeQuery();

        if(rs.next()) {
            return rs.getString("username");
        }else{
            return null;
        }
    }

    // 修改密码
    public static void modifyPassword(String username) throws SQLException {
        Connection connection = getConnection();
        System.out.println("please enter your new password: ");
        String password = sc.nextLine();
        String sql = "update user set password = ? where username = ?";
        PreparedStatement ps = connection.prepareStatement(sql);
        ps.setString(1, password);
        ps.setString(2, username);
        int i = ps.executeUpdate();
        if (i > 0) {
            System.out.println("password modified successfully");
        }else{
            System.out.println("password modification failed");
        }


    }

    // 打印菜单
    public static int menu(String username) {
        System.out.println("Student Management System V2.0");
        System.out.println("Current User: " + username);
        System.out.println("1. Add Student");
        System.out.println("2. Query Student");
        System.out.println("3. Modify Student");
        System.out.println("4. Delete Student");
        System.out.println("5. Statistic Student");
        System.out.println("6. Modify Password");
        System.out.println("7. Exit");
        System.out.print("Please Enter your choice: ");
        Scanner sc = new Scanner(System.in);
        return sc.nextInt();
    }

    // 增加学生
    public static void addStudent() throws SQLException {
        Connection connection = getConnection();
        ArrayList<String> student;

        String sql_1 = "select * from student where id = ?";
        PreparedStatement stmt_1 = connection.prepareStatement(sql_1);
        // 判断ID是否重复
        while (true){
            student = getStudentInfo();
            stmt_1.setString(1, student.get(0));
            ResultSet rs = stmt_1.executeQuery();
            if (rs.next()) {
                System.out.println("The id was exit, please retry ");
            }else{
                break;
            }
        }
        //  插入数据
        String sql = "insert into student values(?,?,?,?,?,?,?)";
        PreparedStatement stmt = connection.prepareStatement(sql);
        stmt.setString(1, student.get(0));
        stmt.setString(2, student.get(1));
        stmt.setString(3, student.get(2));
        stmt.setString(4, student.get(3));
        stmt.setString(5, student.get(4));
        stmt.setString(6, student.get(5));
        stmt.setString(7, student.get(6));
        int row = stmt.executeUpdate();
        if(row > 0){
            System.out.println("Student Added Successfully");
        }else {
            System.out.println("Student Not Added ");
        }
        connection.close();
    }

    // 查询学生
    public static void queryStudent() throws SQLException {
        Connection connection = getConnection();
        System.out.println("which way do you want to query? ");
        System.out.println("1. By Id");
        System.out.println("2. By Province");
        System.out.print("Select your choice: ");
        int choice = sc.nextInt();
        sc.nextLine();
        // 声明变量
        String sql;
        ResultSet res;
        PreparedStatement stmt;

        switch (choice) {
            case 1:
                System.out.println("Please enter student ID: ");
                String id = sc.nextLine();
                // 编写sql
                sql = "select * from student where id = ?";
                stmt = connection.prepareStatement(sql);
                // 设置占位符参数
                stmt.setString(1, id);
                res = stmt.executeQuery();
                // 打印结果
                printInfo(res);
                break;
            case 2:
                System.out.println("Please enter student province: ");
                String province = sc.nextLine();
                // 编写sql
                sql = "select * from student where province = ?";
                stmt = connection.prepareStatement(sql);
                // 设置占位符参数
                stmt.setString(1, province);
                res = stmt.executeQuery();
                printInfo(res);
            default:
                System.out.println("invalid choice");
        }
    }

    //修改学生信息
    public static void modifyStudent() throws SQLException {
        Connection connection = getConnection();

        String sql_1 = "select * from student where id = ?";
        PreparedStatement stmt_1 = connection.prepareStatement(sql_1);
        String id;
        // 判断学生是否存在
        while (true){
            System.out.println("Please enter the id of the student you want to modify: ");
            id = sc.nextLine();
            stmt_1.setString(1, id);
            ResultSet rs = stmt_1.executeQuery();
            if (!rs.next()) {
                System.out.println("The student was not exit, please retry ");
            }else{
                break;
            }
        }
        ArrayList<String> student = getStudentInfo();
        String sql = "update student set name = ? ,gender = ?, phone = ?, " +
                "province = ?, party = ?, born = ? where id = ?";
        PreparedStatement stmt = connection.prepareStatement(sql);
        stmt.setString(1, student.get(1));
        stmt.setString(2, student.get(2));
        stmt.setString(3, student.get(3));
        stmt.setString(4, student.get(4));
        stmt.setString(5, student.get(5));
        stmt.setString(6, student.get(6));
        stmt.setString(7, id);
        int row = stmt.executeUpdate();
        if(row > 0){
            System.out.println("Student Modify Successfully");
        }else {
            System.out.println("Student Not Modify ");
        }
        connection.close();
    }

    // 删除学生信息
    public static void deleteStudent() throws SQLException {
        Connection connection = getConnection();

        String sql_1 = "select * from student where id = ?";
        PreparedStatement stmt_1 = connection.prepareStatement(sql_1);
        String id;
        // 判断学生是否存在
        while (true){
            System.out.println("Please enter the id of the student you want to delete: ");
            id = sc.nextLine();
            stmt_1.setString(1, id);
            ResultSet rs = stmt_1.executeQuery();
            if (!rs.next()) {
                System.out.println("The student was not exit, please retry ");
            }else{
                break;
            }
        }

        String sql = "delete from student where id = ?";
        PreparedStatement stmt = connection.prepareStatement(sql);
        stmt.setString(1, id);
        int row = stmt.executeUpdate();
        if(row > 0){
            System.out.println("Student Deleted Successfully");

        }else {
            System.out.println("Student Not Deleted ");
        }

        connection.close();
    }

    public static void statisticsStudent() throws SQLException {
        Connection connection = getConnection();
        System.out.println("which do you want to statistics? ");
        System.out.println("1. By gender");
        System.out.println("2. By Province");
        System.out.print("Select your choice: ");
        int choice = sc.nextInt();
        sc.nextLine();
        // 声明变量
        String sql;
        ResultSet res;
        PreparedStatement stmt;

        switch (choice) {
            case 1:
                System.out.println("Please enter student gender: ");
                String gender = sc.nextLine();
                // 编写sql
                sql = "select count(*)  from student where gender = ?";
                stmt = connection.prepareStatement(sql);
                // 设置占位符参数
                stmt.setString(1, gender);
                res = stmt.executeQuery();
                // 打印结果
                res.next();
                System.out.println("the number of " + gender + " student: " + res.getString(1));
                break;
            case 2:
                System.out.println("Please enter student province: ");
                String province = sc.nextLine();
                // 编写sql
                sql = "select count(*) from student where province = ?";
                stmt = connection.prepareStatement(sql);
                // 设置占位符参数
                stmt.setString(1, province);
                res = stmt.executeQuery();
                res.next();
                System.out.println("the number of " + province + " province: " + res.getString(1));
            default:
                System.out.println("invalid choice");

        }
    }

    // 键盘读取学生信息
    public static ArrayList<String> getStudentInfo(){
        ArrayList<String> studentInfo = new ArrayList<>();
        System.out.println("please enter student ID: ");
        studentInfo.add(sc.nextLine());
        System.out.println("please enter student Name: ");
        studentInfo.add(sc.nextLine());
        System.out.println("please enter student gender: ");
        studentInfo.add(sc.nextLine());
        System.out.println("please enter student phone: ");
        studentInfo.add(sc.nextLine());
        System.out.println("please enter student province: ");
        studentInfo.add(sc.nextLine());
        System.out.println("please enter student if_party(0/1): ");
        studentInfo.add(sc.nextLine());
        System.out.println("please enter student born: ");
        studentInfo.add(sc.nextLine());

        return studentInfo;
    }


    // 打印学生信息
    public static void printInfo(ResultSet res) throws SQLException {
        if (!res.next()) {
            System.out.println("Student Info Not Found");
        } else {
            do {
                String id = res.getString("id");
                String name = res.getString("name");
                String gender = res.getString("gender");
                String phone = res.getString("phone");
                String province = res.getString("province");

                // 检查列值是否为 NULL
                String part = res.getString("party").equals("1") ? "is_party" : "not_party";
                String born = res.getString("born");
                // 打印结果
                System.out.println(id + "\t" + name + "\t" + gender + "\t" + phone + "\t" + province + "\t" + part + "\t" + born);
            } while (res.next());
        }

    }
}
