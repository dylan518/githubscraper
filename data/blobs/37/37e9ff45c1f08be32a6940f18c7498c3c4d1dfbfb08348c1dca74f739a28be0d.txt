package fc.java.course2.part2;

import fc.java.model2.MovieDTO;

import java.util.ArrayList;
import java.util.List;

public class ArrayListGeneric {
    public static void main(String[] args) {
        List<MovieDTO> list = new ArrayList<>(5); ///moviedto배열
        list.add(new MovieDTO("title",111));
        list.add(new MovieDTO("졸려",555));
        //한가지 타입이 아니라 여러가지 타입을 넣을 수 있기 떄문에
        // 제네릭을 쓰지 않았기 때문에 안전성이 떨어진다.
        System.out.println(list.get(0));
        System.out.println(list.get(1)) ;//서로 다른 타입이 나온다.
    }
}
