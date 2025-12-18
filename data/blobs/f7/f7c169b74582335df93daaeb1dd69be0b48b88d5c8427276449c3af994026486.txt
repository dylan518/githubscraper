package com.yang.algorithm.demo.entropy;

import cn.hutool.core.io.FileUtil;
import org.apache.commons.lang3.StringUtils;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexTest {

    public static void main(String[] args) {

        List<List<Double>> dataList = new ArrayList<>();
        String path = System.getProperty("user.dir") + File.separator + "algorithm-demo" + File.separator + "data" + File.separator + "test.txt";

        //从文件中读取每一行的UTF-8编码数据
        ArrayList<String> readUtf8Lines = FileUtil.readUtf8Lines(path, new ArrayList<>());

        for (int i = 0; i < 5; i++) {
            if (i == 2) {
                continue;
            }
            List<Double> dataNumList = new ArrayList<>();
            for (String readUtf8Line : readUtf8Lines) {

                String data = "";
                Pattern pattern = Pattern.compile("\\[([^\\]]+)\\]");
                Matcher matcher = pattern.matcher(readUtf8Line);
                while (matcher.find()) {
                    data = matcher.group(1);
                }
                if (StringUtils.isNoneBlank(data)) {
                    String[] splits = data.split(" ");
                    dataNumList.add(Double.valueOf(splits[i]));
                }
            }
            dataList.add(dataNumList);
        }


//        ShangFactory shangFactory = new ShangFactory(dataList);
//        List<Double> weightList = shangFactory.listWeight();

        List<Double> weightList = Entropy.getWeight(dataList);

        // 获取权重
        System.err.println("权重:" + weightList);
        for (Double double1 : weightList) {
            System.out.println(double1);
        }
    }
}
