package com.itheima.myiotest1;

import cn.hutool.core.io.FileUtil;
import cn.hutool.core.util.ReUtil;
import cn.hutool.http.HttpUtil;

import java.util.*;

public class Test2 {
    public static void main(String[] args) {
        String familyNameNet = "https://hanyu.baidu.com/shici/detail?pid=0b2f26d4c0ddb3ee693fdb1137ee1b0d&from=kg0";
        String boyNameNet = "http://www.haoming8.cn/baobao/10881.html";
        String girlNameNet = "http://www.haoming8.cn/baobao/7641.html";

        String familyNameStr = HttpUtil.get(familyNameNet);
        String boyNameStr = HttpUtil.get(boyNameNet);
        String girlNameStr = HttpUtil.get(girlNameNet);

        List<String> familyNameTempList = ReUtil.findAll("(.{4})(，|。)", familyNameStr, 1);
        List<String> boyNameTempList = ReUtil.findAll("([\\u4E00-\\u9FA5]{2})(、|。)", boyNameStr, 1);
        List<String> girlNameTempList = ReUtil.findAll("(.. ){4}..", girlNameStr, 0);

        //familyNameTempList(姓氏)
        //处理方案: 把每一个姓氏拆开并添加到一个新的集合当中
        ArrayList<String> familyNameList = new ArrayList<>();
        for (String f : familyNameTempList) {
            for (int i = 0; i < f.length(); i++) {
                char c = f.charAt(i);
                familyNameList.add(c + "");
            }
        }

        //boyNameTempList(男生的名字)
        //处理方案:去除其中的重复元素
        ArrayList<String> boyNameList = new ArrayList<>();
        for (String b : boyNameTempList) {
            if(!boyNameList.contains(b)){
                boyNameList.add(b);
            }
        }

        //girlNameTempList(女生的名字)
        //处理方案:把里面的每一个元素用空格进行分割, 得到每一个女生的名字
        ArrayList<String> girlNameList = new ArrayList<>();
        for (String g : girlNameTempList) {
            String[] arr = g.split(" ");
            girlNameList.addAll(Arrays.asList(arr));
        }

        //5.生成数据
        //姓名(唯一)-性别-年龄
        ArrayList<String> list = getInfos(familyNameList, boyNameList, girlNameList, 10, 10);
        Collections.shuffle(list);

        FileUtil.writeLines(list, "name.txt", "UTF-8");
    }

    public static ArrayList<String> getInfos(ArrayList<String> familyNameList, ArrayList<String> boyNameList, ArrayList<String> girlNameList, int boyCount, int girlCount){
        //1.生成男生不重复的名字
        HashSet<String> boyhs = new HashSet<>();
        while (true) {
            if(boyhs.size() == boyCount){
                break;
            }
            //随机
            Collections.shuffle(familyNameList);
            Collections.shuffle(boyNameList);
            boyhs.add(familyNameList.get(0) + boyNameList.get(0));
        }

        //2.生成女生不重复的名字
        HashSet<String> girlhs = new HashSet<>();
        while (true) {
            if(girlhs.size() == girlCount){
                break;
            }
            Collections.shuffle(familyNameList);
            Collections.shuffle(girlNameList);
            girlhs.add(familyNameList.get(0) + girlNameList.get(0));
        }

        ArrayList<String> res = new ArrayList<>();
        Random r = new Random();
        //3.生成男生的信息并添加到集合当中
        for (String boy : boyhs) {
            int age = r.nextInt(10) + 18;
            res.add(boy + "-男-" + age);
        }
        //4.生成女生的信息并添加到集合当中
        for (String girl : girlhs) {
            int age = r.nextInt(8) + 18;
            res.add(girl + "-女-" + age);
        }
        return res;
    }
}
