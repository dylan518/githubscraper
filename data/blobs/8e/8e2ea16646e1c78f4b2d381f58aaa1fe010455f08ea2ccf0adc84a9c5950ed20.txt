package com;

import com.po.ResultTo;
import dao.AbstractDaoImpl;
import org.MultipartFile;

import java.io.File;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class zixun {
    String driver ="com.mysql.cj.jdbc.Driver";
    String url = "jdbc:mysql://localhost:3306/test";
    String user = "root";
    String pass = "2212165";
    AbstractDaoImpl abstractDao = new AbstractDaoImpl(driver,url,user,pass);


    public List news(String date, Integer pagenow){
        Integer PAGESIZE = 100;
        Integer start = (pagenow-1)*PAGESIZE;
        return abstractDao.getMaps("news","*","date ="+date,start.toString(),PAGESIZE.toString());
    }

    public List discuss(String date, Integer pagenow){
        Integer PAGESIZE = 100;
        Integer start = (pagenow-1)*PAGESIZE;

        return abstractDao.getMaps("discuss","*","date='"+date+"'",start.toString(),PAGESIZE.toString());
    }

    public List<Map<String, Object>> stockorder(String date) {
        List<Map<String, Object>> maps = new ArrayList<>();
        try {

            Connection connection = DriverManager.getConnection(url, user, pass);
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("select zhangfu,gpname from stock where yyyymmdd="+date+" and yyyymmdd = '" + date + "' ORDER BY CONVERT(zhangfu, DECIMAL(10, 8)) DESC");
            Integer i=0;
            while (rs.next()){
                Map<String,Object> map = new HashMap<>();
                String gpName = rs.getString("gpname");
                Float zhangfu = rs.getFloat("zhangfu");
                if(zhangfu>100){continue;}
                if(i>9){break;}
                map.put("gpname",gpName);
                map.put("zhangfu",zhangfu);
                maps.add(map);
                i++;
            }
            rs.close();
            statement.close();
            connection.close();
        }catch (Exception e){
            e.printStackTrace();
        }
        return maps;
    }

    public List<Map<String, Object>> longhu(String date) {
        List<Map<String, Object>> maps = new ArrayList<>();
        try {

            Connection connection = DriverManager.getConnection(url, user, pass);
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("select * from stock where yyyymmdd="+date+" and ((highprice-lowprice)/lowprice) > 0.1 and zhangfu>0 order by ((highprice-lowprice)/lowprice) desc limit 0,5");

            while (rs.next()){
                Map<String,Object> map = new HashMap<>();
                String gpName = rs.getString("gpname");
                Long volume = rs.getLong("volume");
                Float zhangfu = rs.getFloat("zhangfu");
                map.put("gpname",gpName);
                map.put("volume",volume);
                map.put("zhangfu",zhangfu);
                maps.add(map);
            }
            rs.close();
            statement.close();
            connection.close();
        }catch (Exception e){
            e.printStackTrace();
        }
        return maps;
    }

    public List<Map<String, Object>> longhu3(String date) {
        Integer d = Integer.parseInt(date)-2;
        String date2 = Integer.toString(d);

        List<Map<String, Object>> maps = new ArrayList<>();
        try {
            Connection connection = DriverManager.getConnection(url, user, pass);
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery("select gpname from stock where yyyymmdd <='"+date+"' and yyyymmdd >='"+date2+"' group by gpname having sum(zhangfu)>20 and count(*)=3");
            List<String> gps=new ArrayList<>();
            while (rs.next()){
                String gpName = rs.getString("gpname");
                gps.add(gpName);
            }
            String gpss = "('"+String.join("','", gps)+"')";
            Statement statement1= connection.createStatement();
            ResultSet rs1 = statement1.executeQuery("select gpname,zhangfu,volume from stock where yyyymmdd ='"+date+"' and gpname in "+gpss);

            while(rs1.next()) {
                Map<String,Object> map = new HashMap<>();
                String gpName = rs1.getString("gpname");
                Long volume = rs1.getLong("volume");
                Float zhangfu = rs1.getFloat("zhangfu");
                map.put("gpname", gpName);
                map.put("volume", volume);
                map.put("zhangfu", zhangfu);
                maps.add(map);
            }
            rs.close();
            rs1.close();
            statement.close();
            statement1.close();
            connection.close();
        }catch (Exception e){
            e.printStackTrace();
        }
        return maps;
    }
}
