package com.donation.exercise.Exceptions;

import lombok.Getter;

@Getter
public enum ErrMsg {
  ID_ALREADY_EXISTS("id already exists"),
  PRICE_ERROR("donation is not under 180 NIS"),
  PRICE_ERROR_2("donation is not more than 1800 NIS"),
  ID_NOT_FOUND("Id not found");
  private String msg;
    ErrMsg(String msg){this.msg=msg;}
}
