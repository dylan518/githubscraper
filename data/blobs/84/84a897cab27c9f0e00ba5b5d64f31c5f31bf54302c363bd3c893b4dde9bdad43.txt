/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mkl.mybatisrep.datasource;

import com.mkl.mybatisrep.Mybatisrep;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
//import org.apache.ibatis.datasource.pooled.PooledDataSource;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

/**
 *
 * @author agung
 */
public class DataSourceFactory {

    public static String driverclassname;
    //public static String datasourceclassName;
    public static String url;
    public static String username;
    public static String password;
    private static HikariConfig config = new HikariConfig();
    private static HikariDataSource ds;

    private static void decryptPassword() throws FileNotFoundException {
        FileInputStream stream = null;
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("123456789");
        encryptor.setAlgorithm("PBEWITHMD5ANDDES");
        Properties prop = new Properties();
        stream = new FileInputStream(Mybatisrep.appConfigPath());
        try {
            prop.load(stream);
            driverclassname = prop.getProperty("jdbc.driverclassname");
            //datasourceclassName = prop.getProperty("jdbc.datasourceclassname");
            url = prop.getProperty("jdbc.url") + "?useUnicode=yes&characterEncoding=UTF-8&useSSL=false";
            username = prop.getProperty("jdbc.username");
            password = encryptor.decrypt(prop.getProperty("jdbc.password"));
        } catch (IOException ex) {
            //eat all error
        } finally {
            try {
                stream.close();
            } catch (IOException ex) {
                Mybatisrep.getLogger().error(ex.getMessage());
            }
        }
    }

    public static HikariDataSource getDataSource() throws FileNotFoundException {
        decryptPassword();
        config.setJdbcUrl(url);
        config.setUsername(username);
        config.setPassword(password);
        config.setDriverClassName(driverclassname);
        /*
        config.setDriverClassName(driverclassname);
        config.setMaximumPoolSize(20);
        config.addDataSourceProperty("cachePrepStmts", "true");
        config.addDataSourceProperty("prepStmtCacheSize", 250);
        config.addDataSourceProperty("prepStmtCacheSqlLimit", 2048);
        */
        config.addDataSourceProperty("useJDBCCompliantTimezoneShift", "true");
        config.addDataSourceProperty("useLegacyDatetimeCode", "false");
        config.addDataSourceProperty("serverTimezone", "UTC");
        config.addDataSourceProperty("maximumPoolSize", 20);
        config.addDataSourceProperty("cachePrepStmts", "true");
        config.addDataSourceProperty("prepStmtCacheSize", 250);
        config.addDataSourceProperty("prepStmtCacheSqlLimit", 2048);
        ds = new HikariDataSource(config);
        return ds;
    }

    public static void closeConnection() {
        ds.close();
    }
}
