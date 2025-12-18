package com.jilingy.deep.learning.common.enums;

import cn.hutool.core.date.CalendarUtil;
import cn.hutool.core.date.DateField;
import cn.hutool.core.util.StrUtil;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Optional;
import java.util.regex.Pattern;

/**
 * @author: YangJiling
 * @Description:
 * @date: 2022-10-23
 */
public enum DateTypeEnum {

    /**
     * 日
     */
    DAY("day", "D", "日", Pattern.compile("([0-9]{4})(-)(0[1-9]|1[012])(-)(0[1-9]|[12][0-9]|3[01])"), "yyyy-MM-dd", "PREDICTED_LOAD_DAY",
            DateField.HOUR),
    /**
     * 月
     */
    MONTH("month", "M", "月", Pattern.compile("([0-9]{4})(-)(0[1-9]|1[012])"), "yyyy-MM", "PREDICTED_LOAD_MONTH", DateField.DAY_OF_MONTH),

    /**
     * 年
     */
    YEAR("year", "Y", "年", Pattern.compile("([0-9]{4})"), "yyyy", "PREDICTED_LOAD_YEAR", DateField.MONTH),

    /**
     * 小时
     */
    HOUR("hour", "H", "小时", Pattern.compile("([0-9]{4})"), "yyyy-MM-dd HH:mm:ss", "PREDICTED_LOAD_HOUR", DateField.HOUR),

    /**
     * 日
     */
    DEFINED("day", "N", "日", Pattern.compile("([0-9]{4})(-)(0[1-9]|1[012])(-)(0[1-9]|[12][0-9]|3[01])"), "yyyy-MM-dd", "PREDICTED_LOAD_DAY",
            DateField.HOUR);

    private String type;
    private String typeShort;
    private String name;
    private Pattern timePattern;
    private String strPattern;
    private String componentCode;
    private DateField dateField;

    public static boolean matchDayPattern(String timeStr) {
        return StrUtil.isEmpty(timeStr) ? false : DAY.timePattern.matcher(timeStr).matches();
    }

    public static boolean matchMonthPattern(String timeStr) {
        return StrUtil.isEmpty(timeStr) ? false : MONTH.timePattern.matcher(timeStr).matches();
    }

    public static boolean matchYearPattern(String timeStr) {
        return StrUtil.isEmpty(timeStr) ? false : YEAR.timePattern.matcher(timeStr).matches();
    }

    public static boolean validateTimeStr(String timeStr, String type) {
        if (StrUtil.isEmpty(timeStr)) {
            return false;
        } else {
            return StrUtil.equals(DAY.getType(), type) && matchDayPattern(timeStr) || StrUtil.equals(MONTH.getType(), type) && matchMonthPattern(timeStr) || StrUtil.equals(YEAR.getType(), type) && matchYearPattern(timeStr);
        }
    }

    public static DateTypeEnum getByType(String type) {
        Optional<DateTypeEnum> timeTypeEnum = Arrays.stream(values()).filter((e) -> {
            return StrUtil.equals(e.type, type);
        }).findFirst();
        return timeTypeEnum.isPresent() ? (DateTypeEnum) timeTypeEnum.get() : null;
    }

    public static DateTypeEnum getByTypeB(String typeB) {
        Optional<DateTypeEnum> timeTypeEnum = Arrays.stream(values()).filter((e) -> {
            return StrUtil.equals(e.typeShort, typeB);
        }).findFirst();
        return timeTypeEnum.isPresent() ? (DateTypeEnum) timeTypeEnum.get() : null;
    }

    public static Calendar getBegin(Calendar calendar, String type) {
        DateTypeEnum timeType = getByType(type);
        switch (timeType) {
            case YEAR:
                CalendarUtil.beginOfYear(calendar);
                break;
            case MONTH:
                CalendarUtil.beginOfMonth(calendar);
                break;
            case HOUR:
                CalendarUtil.truncate(calendar, DateField.HOUR);
                break;
            case DAY:
            default:
                CalendarUtil.beginOfDay(calendar);
        }

        return calendar;
    }

    public static Calendar getEnd(Calendar calendar, String type) {
        DateTypeEnum timeType = getByType(type);
        switch (timeType) {
            case YEAR:
                CalendarUtil.endOfYear(calendar);
                break;
            case MONTH:
                CalendarUtil.endOfMonth(calendar);
                break;
            case HOUR:
                CalendarUtil.ceiling(calendar, DateField.HOUR);
                break;
            case DAY:
            default:
                CalendarUtil.endOfDay(calendar);
        }

        return calendar;
    }

    public static void addOffSetByType(Calendar calendar, String type, int offset) {
        if (StrUtil.equals(YEAR.getType(), type)) {
            calendar.add(1, offset);
        } else if (StrUtil.equals(MONTH.getType(), type)) {
            calendar.add(2, offset);
        } else {
            calendar.add(5, offset);
        }

    }

    public String getType() {
        return this.type;
    }

    public String getTypeShort() {
        return this.typeShort;
    }

    public String getName() {
        return this.name;
    }

    public Pattern getTimePattern() {
        return this.timePattern;
    }

    public String getStrPattern() {
        return this.strPattern;
    }

    public String getComponentCode() {
        return this.componentCode;
    }

    public DateField getDateField() {
        return this.dateField;
    }

    private DateTypeEnum(String type, String typeShort, String name, Pattern timePattern, String strPattern, String componentCode,
                         DateField dateField) {
        this.type = type;
        this.typeShort = typeShort;
        this.name = name;
        this.timePattern = timePattern;
        this.strPattern = strPattern;
        this.componentCode = componentCode;
        this.dateField = dateField;
    }
}
