package Lesson_2_DAO.task_2.Dao;


import Lesson_2_DAO.task_3.Jewelry.Necklace;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;


public class NecklaceJDBCDAO implements INecklaceDAO {

    @Override
    public List<Necklace> getListOfNecklaces() {
        List<Necklace> necklaces = new ArrayList<>();

        String str = "select id, name from List_of_necklaces;";
        try (Connection connection = getConnection();
             PreparedStatement statement = connection.prepareStatement(str)) {
            ResultSet result = statement.executeQuery();

            while(result.next()) {
                Necklace necklace = new Necklace();
                necklace.setID(result.getInt(1));
                necklace.setName(result.getString(2));

                necklaces.add(necklace);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (NullPointerException e) {
            System.err.println("Помилка з'єднання з базою данних");
        }

        return necklaces;
    }

    public void writeListOfNecklaces(List<Necklace> listOfNecklaces) {
        clearSQLTable();
        for (Necklace necklace : listOfNecklaces)
            writeNecklace(necklace);
    }

    private void writeNecklace(Necklace necklace) {
        String str = "insert into List_of_necklaces (id, name) values (?,?);";

        try (Connection connection = getConnection();
             PreparedStatement statement = connection.prepareStatement(str)) {

            statement.setInt(1, necklace.getID());
            statement.setString(2, necklace.getName());
            statement.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        } catch (NullPointerException e) {
            System.err.println("Помилка з'єднання з базою данних");
        }
    }

    private void clearSQLTable() {
        String str = "delete from List_of_necklaces;";
        try (Connection connection = getConnection();
             PreparedStatement statement = connection.prepareStatement(str)) {

            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (NullPointerException e) {
            System.err.println("Помилка з'єднання з базою данних");
        }
    }


    private Connection getConnection() {
        try {
            return DriverManager.getConnection("jdbc:mysql://localhost:3306/Catalogue_of_necklaces", "root", "root");
        } catch (SQLException e) {
            return null;
        }
    }
}
