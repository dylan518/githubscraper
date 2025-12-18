package com.geominfo.bi;

public class FieldInfo{
    //字段id
    private String fid;

    //维度(row)和度量(column)类型区分
    private AreaType areaType;

    //时间区分(年，月，日，时)
    private DateTrunc dateTrunc;

    //聚合函数名称
    private String aggregate;

    //排序方式 (asc:升序，desc:降序，不排序则为null)
    private SortType sortType;

    public enum AreaType {
        row,
        column,
    }

    public enum DateTrunc {
        year,
        month,
        day,
        hour,
        minute,
        second,
        //季度
        quarter,
        //周
        week
    }

    public enum SortType {
        //升序
        asc,
        //降序
        desc
    }

    public String getFid() {
        return fid;
    }

    public void setFid(String fid) {
        this.fid = fid;
    }

    public AreaType getAreaType() {
        return areaType;
    }

    public void setAreaType(AreaType areaType) {
        this.areaType = areaType;
    }

    public DateTrunc getDateTrunc() {
        return dateTrunc;
    }

    public void setDateTrunc(DateTrunc dateTrunc) {
        this.dateTrunc = dateTrunc;
    }

    public String getAggregate() {
        return aggregate;
    }

    public void setAggregate(String aggregate) {
        this.aggregate = aggregate;
    }

    public SortType getSortType() {
        return sortType;
    }

    public void setSortType(SortType sortType) {
        this.sortType = sortType;
    }
}
