package com.example.adminserver.sys.controller;

import com.example.adminserver.sys.util.GetData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataController {

    @Autowired
    private GetData getData;

    @GetMapping("/data/{id}")
    public String getData(@PathVariable String id) {
        // 调用GetData服务来获取数据（会自动缓存）
        return getData.getData(id);
    }

    @GetMapping("/set/{id}")
    public void setData(@PathVariable String id) {
        // 调用GetData服务来获取数据（会自动缓存）
        getData.setData(id);
    }

    @GetMapping("/clearCache/{id}")
    public String clearCache(@PathVariable String id) {
        // 手动清除缓存
        getData.clearCache(id);
        return "Cache for " + id + " has been cleared.";
    }
}
