package com.demo.model;

import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;
import java.util.List;

/**
 * @Author huangfeng
 * @Date 2023/10/28 16:17
 * @description
 * @Version 1.0
 */
@Getter
@Setter
public class DeeplQueryParamDTO implements Serializable {
    private List<String> text;
    private String target_lang;

    public DeeplQueryParamDTO() {
    }

    public DeeplQueryParamDTO(List<String> text, String target_lang) {
        this.text = text;
        this.target_lang = target_lang;
    }
}
