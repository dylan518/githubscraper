package HashMapAndTreeSet;

import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;
import java.util.TreeSet;

/**
 * K번째 큰 수
 *
 * 현수는 1부터 100까지의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 카드의 수가 여러장 있을 수 있습니다. 현수는 이중 3장을 뽑아
 * 각 카드의 적힌 수를 합한 값을 기록 하려고 합니다 . 3장을 뽑은 모든 경우의 수를 기록합니다. 기록한 값중 K번째로 큰 수를 기록하는 프로그램을 작성하세요
 * 만약 큰 수 부터 만들어진 수가  25 25 23 23 22 20 19 ... 이고 k의 값이 3이라면 k번째 큰 값은 22입니다.
 *
 * @임력설명: 첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음줄에 N개의 카드값이 입력된다.
 * @출력설명: 첫 줄에 K번째 수를 출력합니다. K번째 수가 존재하지 않으면 -1를 출력합니다
 *
 * @입력예제: 10 3
 *          13 15 34 23 45 65 33 11 26 42
 * @출력예제: 143
 * */
public class K번째큰수 {
    /*정렬을 하기위한 트리셋 */
    public int solution(int[] arr, int n, int k){
        int answer = 0;
        //Collections.reverseOrder() 이게 없으면 오름차순이지만 이걸 쓰면 내림차순으로 자동정렬함
        TreeSet<Integer> Tset = new TreeSet<>(Collections.reverseOrder());
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                for(int l=j+1; l<n; l++){
                    Tset.add(arr[i]+arr[j]+arr[l]);
                }
            }
        }
        int cnt = 0;
        //Tset.remove(143);
        System.out.println(Tset.size()); //원소의 갯수
        System.out.println(Tset.first()); //오름차순이면 최소값을 받고 내림차순이면 최대값을 받음 첫숫자 43
        System.out.println(Tset.last()); //오름차순이면 최소값을 받고 내림차순이면 최대값을 받음 마지막 숫자 143
        for(int x : Tset){
            System.out.println(x);//누가 지워진지 보려구
            cnt++;
            if(cnt==k) return answer;
            System.out.println(cnt+ " "+x);
        }
        return answer;

    }
    public static void main(String[] args) {
        K번째큰수 T = new K번째큰수();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int k = kb.nextInt();
        int[] arr= new int[n];
        for(int i=0; i<n; i++){
            arr[i]=kb.nextInt();
        }
        System.out.println(T.solution(arr, n, k));
    }
}
/* 오늘은 쉬어가는날 */
