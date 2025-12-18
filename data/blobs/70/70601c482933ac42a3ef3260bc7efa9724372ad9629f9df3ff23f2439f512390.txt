package com.zys.design.pattern.adapter;

import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalDateTime;

/**
 * @Description 日志实体类
 * @Author leo
 * @Date 2020/8/26 14:05
 */
public class Log implements Serializable {
    /**
     * 日志ID
     */
    private String logId;
    /**
     * 创建时间
     */
    private LocalDateTime createTime;
    /**
     * 日志记录用户
     */
    private String userName;

    public String getLogId() {
        return logId;
    }

    public void setLogId(String logId) {
        this.logId = logId;
    }

    public LocalDateTime getCreateTime() {
        return createTime;
    }

    public void setCreateTime(LocalDateTime createTime) {
        this.createTime = createTime;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    @Override
    public String toString() {
        return "Log{" +
                "logId='" + logId + '\'' +
                ", createTime=" + createTime +
                ", userName='" + userName + '\'' +
                '}';
    }
}
