package com.yqy.spring.jdbc;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.test.context.junit.jupiter.SpringJUnitConfig;

import java.util.List;

@SpringJUnitConfig(locations = "classpath:beans.xml")
public class JdbcTemplateTest {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    /**
     * 查询操作
     */
    //查询：返回对象
    @Test
    public void testSelectObject() {
        //写法1
        /*String sql = "select * from t_emp where id = ?";
        Emp emoResult = jdbcTemplate.queryForObject(sql,
            (rs, rowNum) -> {
                Emp emp = new Emp();
                emp.setId(rs.getInt("id"));
                emp.setName(rs.getString("name"));
                emp.setAge(rs.getInt("age"));
                emp.setSex(rs.getString("sex"));
                return emp;
        }, 2);
        System.out.println(emoResult);*/

        //写法2
        String sql = "select * from t_emp where id = ?";
        Emp emp = jdbcTemplate.queryForObject(sql,
                new BeanPropertyRowMapper<>(Emp.class),2);
        System.out.println(emp);
    }

    //查询：返回list集合
    @Test
    public void testSelectList() {
        String sql = "select * from t_emp where id = ?";
        List<Emp> list = jdbcTemplate.query(sql, new BeanPropertyRowMapper<>(Emp.class), 2);
        System.out.println(list);
    }

    //查询：返回单个值
    @Test
    public void testSelectValue(){
        String sql = "select count(*) from t_emp";
        Integer count = jdbcTemplate.queryForObject(sql, Integer.class);
        System.out.println(count);
    }


    /**
     * 数据库的增加 修改 删除操作
     */
    @Test
    public void testUpdate() {
        //1 添加操作
        /*String sql = "INSERT INTO t_emp VALUES(NULL,?,?,?)";
        Object[] params = {"yqy", "20", "男"};
        int rows = jdbcTemplate.update(sql,params);
        System.out.println(rows);*/

        //2 修改操作
        /*String sql = "UPDATE t_emp SET name = ? WHERE id = ?";
        int rows = jdbcTemplate.update(sql,"xuebao",3);
        System.out.println(rows);*/

        //3 删除操作
        String sql = "DELETE FROM t_emp WHERE id = ?";
        int rows = jdbcTemplate.update(sql,1);
        System.out.println(rows);
    }
}








