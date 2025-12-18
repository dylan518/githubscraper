package com.tz.leo.springboot.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.OutputStream;
import java.util.List;
import java.util.Map;

/**
 * Author: tz_wl
 * Date: 2020/7/11 19:29
 * Content:
 */
@RequestMapping("hello04")
@RestController
public class Hello04Controller {

    @Value("${name}")
    private String name;

    @Value("${age}")
    private String age;

    @Value("${qqs}")
    private String[] qqs;

    @Value("#{'${strs}'.split(',')}")
    private List<String> strs;

    @Value("#{${map}}")
    private Map<String,String> map;


    /**
     *
     * http://localhost:8085/sb/hello04/hello01
     */
    @RequestMapping("hello01")
    public String Hello01(){
        System.out.println("hello 0401 ");

        System.out.println("name and age is : "+name +"_"+ age );

        // 打印数组
        for (String qq : qqs) {
            System.out.println("qq is: "+  qq);
        }

        //打印集合
        strs.forEach(str-> System.out.println(str));

        //打印map
        map.forEach((k,v)-> System.out.println("k = " + k + "v="+v));

        System.out.println("******************");
        return "@Value(\"${name}\")   方式从application.yml 中注入数值 ，包括注入基本类型" +
                "注入数组 注入集合 注入map ";
    }

}
