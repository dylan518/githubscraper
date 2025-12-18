package d_collections;

import java.util.ArrayList;
import java.util.LinkedList;

public class List {
    public static void main(String[] args) {
        
        /* List Interface
         * 리스트 계열의 컬렉션은 저장 요소를 순차적으로 관리하며 중복된 값과 null값을 요소로 허용한다.
         * 요소에 대한 접근은 배열과 동일하게 인덱스로 접근한다.
         * 리스트 인터페이스를 구현한 대표 클래스는 ArrayList, LinkedLIst, Vector 클래스가 있다.
         */

         /* ArrayList
          * ArrayList는 내부에 배열을 갖고 있다. 따라서 고정 길이 저장공간으로 요소들을 관리한다.
          * ArrayList의 내부 배열이 요소를 담을 수 있는 용량을 capacity라고 한다.
          * 내부 배열 용량을 이상을 저장할 경우, 내부적으로 용량을 늘린 새로운 배열을 만들어 요소를 담는다.
          */

        ArrayList<String> list = new ArrayList<>();

        list.add("test");
        list.add("success");
        list.add(1,"chnage"); // 데이터 변경

        /*
         * 리스트 중간 요소 추가, 삭제시 자동으로 이후 인덱스를 뒤로 밀거나, 빈 인덱스로 데이터를 당겨온다.
         * 떄문에 추가, 삭제가 빈번한 데이터의 관리에는 적합하지 않다.
         */

        /* LinkedList
         * 짒합하는 각 요소들을 노드로 표현하고 각 도드들을 서로 연결하여 리스트를 구성한다.
         * 요소를 갖는 각 노드들은 다음 노느데 대한 참조정보를 통해 접근한다.
         * 노드는 필요할 경우 만들어서 연결하여 사용하기 때문에, 미리 정의된 용량(capacity)의 개념이 없다.
         * List 인터페이스를 구현한 다른 클래스들과 마찬가지로 인덱스를 통해 요소에 접근한다.
         * 인덱스를 사용하여 데이터에 접근한다.
         */

        LinkedList<String> linkL = new LinkedList<>();
        
        linkL.add("tt");
        linkL.add("show");
        linkL.add(0,"third");

        /* 리스트 인터페이스로 구현한 자료구조는 add()로 추가하고 get(index)으로 값을 가져온다.*/
    }
    
}
