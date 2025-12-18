package com.myz.inf.constant.demo;

import com.myz.inf.constant.ConfigurableConstantsHelper;
import com.myz.inf.constant.ConfigurableConstantsManager;
import com.myz.inf.constant.dao.ConstantConfigMapper;
import com.myz.inf.constant.demo.dao.UserLogMapper;
import com.myz.inf.constant.demo.domain.UserLog;
import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.test.context.jdbc.Sql;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.transaction.annotation.Transactional;

import javax.sql.DataSource;
import java.util.List;

/**
 * @author zhaomingyu
 * 2022/6/30
 */
@RunWith(SpringRunner.class)
@SpringBootTest(classes = MyTestConfiguration.class)
@Transactional
@Rollback
public class TestConfigurableConstant {

    @Autowired
    private DataSource dataSource;

    @Autowired
    private ConstantConfigMapper constantConfigMapper;

    @Autowired
    private ConfigurableConstantsManager configurableConstantsManager;

    @Autowired
    private ConfigurableConstantsHelper configurableConstantsHelper;

    @Autowired
    private UserLogMapper userLogMapper;

    @Test
    @Sql(value = { "classpath:data/init.sql"})
    public void testConstant() {
        // init constantHelper
        configurableConstantsManager.setConstantConfigMapper(constantConfigMapper);
        configurableConstantsHelper.setConfigurableConstantsManager(configurableConstantsManager);

        PhoneTypeEnum iphone = ConfigurableConstantsHelper.getByCode(PhoneTypeEnum.class, "IPHONE");
        Assert.assertEquals("IPHONE", iphone.code());

        List<UserLog> userLogs = userLogMapper.selectAllUserLog();

        for (UserLog userLog : userLogs) {
            System.out.println(
                    userLog.getUserName() + ", " + userLog.getPhoneType().code() + ", " + userLog.getPhoneType().desc());
        }


    }
}
