package mysql;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        TestingMySQL testingMySQL = new TestingMySQL();

        Connection conn = testingMySQL.getConnection();
        List<User> users;

        try {
             users = testingMySQL.getUsers();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        users.forEach(user -> {
            System.out.println(user);
        });

        testingMySQL.close(conn);
    }




}
