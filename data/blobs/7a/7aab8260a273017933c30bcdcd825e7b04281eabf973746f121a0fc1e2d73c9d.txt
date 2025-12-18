package com.atguigu.cloud.resp;

import lombok.Data;
import lombok.experimental.Accessors;

/**
 * @author LiHongFei
 * @version 1.0
 * @since 2024/7/13
 */
@Data
@Accessors(chain = true)
public class ResultData<T> {
    /**
     * code状态值: 由后端统一定义各种返回结果的状态码
     * message描述: 本次接口调用的结果描述
     * data数据: 本次返回的数据
     * timestamp时间戳: 接口调用的时间戳
     */
    private String code; /*结果状态码，具体状态码参考枚举类ReturnCodeEnum.java*/
    private String message;
    private T data;
    private long timestamp;

    public ResultData() {
        this.timestamp = System.currentTimeMillis();
    }

    public static <T> ResultData<T> success(T data) {
        ResultData resultData = new ResultData();

        resultData.setCode(ReturnCodeEnum.RC200.getCode());
        resultData.setMessage(ReturnCodeEnum.RC200.getMessage());
        resultData.setData(data);

        return resultData;
    }

    public static <T> ResultData<T> fail(String code, String message) {
        ResultData resultData = new ResultData();

        resultData.setCode(code);
        resultData.setMessage(message);
        resultData.setData(null);

        return resultData;
    }
}
