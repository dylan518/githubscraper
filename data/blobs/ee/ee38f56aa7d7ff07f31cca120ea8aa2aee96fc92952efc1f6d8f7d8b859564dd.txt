package exam01;

public class Ex02 {
    public static void main(String[] args) {  // 1. main 함수가 처음으로 실행
//        int n1 = 10;  // add 함수지역에 있는 n1 명칭이 같다해도 서로 주소가 다르다.
//        int n2 = 20;
       int r = add(10,20);  // 담을수 있는 공간(메모리), 이름이 있어야 변수
        // 2. add 함수 실행 후 종료(스택 제거)되면, main 함수도 실행 종료(스택 제거)
        System.out.println(r);
    }

                      // 함수 지역 (지역변수)
    static int add(int n1, int n2){
     int result = n1 + n2;
            return result;
    }  // 함수가 실행될때 메모리에 할당 받고, 실행후에 메모리에서 소멸된다.
}
