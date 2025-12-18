package com.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.bean.Subject;
import com.resource.LaDbConnection;

public class SubjectDao {

	public static List<Subject> list() throws SQLException {
        List<Subject> listSubject = new ArrayList<>();
         
        try (Connection conn = LaDbConnection.getLaDbConn()) {
            
            PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM Subject ORDER BY subjectName");
            ResultSet resultSet = pstmt.executeQuery();
             
            while (resultSet.next()) {
                int id = resultSet.getInt("subjectId");
                String name = resultSet.getString("subjectName");
                int teacherId = resultSet.getInt("teacherId");
                Subject subject = new Subject(id, name, teacherId);
                     
                listSubject.add(subject);
            }          
             
        } catch (SQLException ex) {
            ex.printStackTrace();
            throw ex;
        }      
         
        return listSubject;
    }
}
