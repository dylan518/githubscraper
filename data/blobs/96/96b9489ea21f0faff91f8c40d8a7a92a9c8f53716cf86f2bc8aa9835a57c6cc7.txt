package online.danbao.Exam.Exam9;

import online.danbao.test.Main;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;

/**
 * @author: 蛋宝
 * @date: 2022/12/6 23:17
 * @description:
 */
public class tjjyz extends JFrame {

    private static final java.awt.event.ActionListener ActionListener = null;
    JLabel biaoqian1,biaoqian2,biaoqian3,biaoqian4;
    JTextField text1,text2,text3,text4;
    JButton button1,button2;
    protected String sql;
    //	qrlisten listen1;
    public tjjyz() {
        setTitle("用户注册");
        setLayout(null);

        this.setBounds(500,500,300,300);
        this.setVisible(true);

        biaoqian1 = new JLabel("用户名");
        add(biaoqian1);
        biaoqian1.setBounds(10,10,100,20);

        text1 = new JTextField(10);
        add(text1);
        text1.setBounds(40,10,100,20);

        biaoqian2 = new JLabel("密码");
        add(biaoqian2);
        biaoqian2.setBounds(10, 30, 100, 20);

        text2 = new JPasswordField(10);
        add(text2);
        text2.setBounds(40,30,100,20);

        button1 = new JButton("保存");
        add(button1);
        button1.setBounds(20, 90, 60, 20);

        button2 = new JButton("取消");
        add(button2);
        button2.setBounds(90, 90, 60, 20);



        button1.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e)  {
                Driver driver = null;                       //1.驱动注册
                try {
//                    driver = new Driver();
                   driver=new com.mysql.cj.jdbc.Driver();
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
                String url = "jdbc:mysql://localhost:3306/scsstudy?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai";  //2.连接的数据库的URL

                Properties info = new Properties();                //3.封装用户名密码
                info.setProperty("user", "root");                  // 将用户名和密码封装在Properties中
                info.setProperty("password", "ldd123789dd");

                Connection connect = null;    //4.获得连接
                try {
                    connect = driver.connect(url, info);
                } catch (SQLException throwables) {
                    throwables.printStackTrace();
                }
                System.out.println(connect);




                //连接调用方法输送sql语句，返回预编译的实例对象
                String sql = "insert into exam09 (name,password) VALUES (?,?)";
                PreparedStatement ps = null;

                try{
                    ps = connect.prepareStatement(sql);
                    ps.setObject(1,text1.getText());
                    ps.setObject(2,text2.getText());
                    //执行sql语句
                    ps.execute();


                    //资源关闭

                    connect.close();
                    ps.close();
                }
                catch (SQLException throwables) {
                    throwables.printStackTrace();
                }


            }
        });
    }}


