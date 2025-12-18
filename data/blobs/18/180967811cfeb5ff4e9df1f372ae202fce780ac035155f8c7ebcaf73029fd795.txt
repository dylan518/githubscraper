package com.jsdc.itss.dao;

import com.jsdc.core.base.BaseDao;
import com.jsdc.itss.model.AssetsClGroup;
import org.apache.commons.lang.StringUtils;
import org.springframework.stereotype.Repository;

/**
 * @Author libin
 * @create 2022-03-08 12:19:43
 */
@Repository
public class AssetsClGroupDao extends BaseDao<AssetsClGroup> {

    public String toList(AssetsClGroup beanParam) {
        StringBuilder sql = new StringBuilder();

        sql.append(" SELECT * ").append(" FROM ").append("assets_cl_group");
        sql.append(" where is_del=0 ");
        if (null != beanParam) {
            if (StringUtils.isNotBlank(beanParam.getGroup_name())) {
                sql.append(" and group_name like '%" + beanParam.getGroup_name() + "%' ");
            }
            if (null != beanParam.getIs_enable()) {
                sql.append(" and is_enable=" + beanParam.getIs_enable());
            }
        }
        return sql.toString();
    }
}
