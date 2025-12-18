package a09datedemo1;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class a09datedemo2 {
    public static void main(String[] args) throws ParseException {
        String start = "2022年11月11日 00:00:00";
        String end = "2022年11月11日 00:10:00";
        String order = "2022年11月11日 00:01:00";
        //解析
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd月 HH:mm:ss");
        Date startdate = sdf.parse(start);
        Date enddate = sdf.parse(end);
        Date orderdata = sdf.parse(order);
        //得到三个时间值
        long starttime = startdate.getTime();
        long endtime = enddate.getTime();
        long ordertime = orderdata.getTime();
        //判断
        if (ordertime >= starttime && ordertime <= endtime) {
            System.out.println("秒杀成功");
        } else {
            System.out.println("秒杀失败");
        }

    }
}
