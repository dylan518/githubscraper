package com.cuit;

import com.cuit.mapper.RoomMapper;
import com.cuit.pojo.Room;
import org.junit.FixMethodOrder;
import org.junit.jupiter.api.Test;
import org.junit.runners.MethodSorters;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;
import java.util.Date;
import java.util.List;

@SpringBootTest
@FixMethodOrder(MethodSorters.NAME_ASCENDING)  //按照指定方法运行
public class RoomTest {

    @Autowired
    DataSource dataSource;

    @Autowired
    RoomMapper roomMapper;

    @Test
    void test() throws SQLException {
        System.out.println(dataSource.getClass());
        Connection connection = dataSource.getConnection();
        connection.close();
    }

    @Test
    public void testA(){
        List<Room> rooms = roomMapper.queryRoomList();
    }

    @Test
    public void testB(){
        Room room = new Room("三食堂",new Date());
        Integer r = roomMapper.addRoom(room);
        List<Room> rooms = roomMapper.queryRoomList();
    }

    @Test
    public void testC(){
        Integer n = roomMapper.deleteRoom(4);
        List<Room> rooms = roomMapper.queryRoomList();
    }
}
