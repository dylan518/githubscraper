package www.itheima.com.collection.Father;

import java.util.ArrayList;
import java.util.Collection;
import java.util.function.Consumer;

public class Lamda {
    public static void main(String[] args) {
        Collection<String> list = new ArrayList<>();
        list.add("111");
        list.add("222");
        list.add("333");

        //在底层也使用到了一个for循环的形式来遍历每一个元素
        //把得到的每一个元素，传递给下面的accept()的方法
        //s就表示集合中的每一个数据。
/*      list.forEach(new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println(s);
            }
        });*/

        //lambda表达式
        list.forEach((String s) -> System.out.println(s));

    }
}
//总结
//1.迭代器:在遍历的过程中需要删除元素，请使用迭代器。迭代器.remove();
//2.增强for、 Lambda:仅仅想遍历，那么使用增强for或Lambda表达式。
