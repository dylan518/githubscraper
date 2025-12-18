import java.util.*;



public class Main {

    public static int k;
    public static int n;
    public static ArrayList<Integer> answer = new ArrayList<>();

    public static void print(){
        for(int i=0; i<answer.size(); i++){
            System.out.print(answer.get(i) + " ");
        }
        System.out.println();
    }


    public static void choose(int curNum){
        // 종료 조건(초기값)
        if(curNum == n+1){  // 1,2,3 채우고 4될 때 종료니까
            print();
            return;
        }

        for(int i=1; i<=k; i++){
            answer.add(i);
            choose(curNum+1);

            // 0갔다가 나오면 다음에 1넣어야하니까 이전에 넣었던 0을 빼야함
            answer.remove(answer.size()-1);    
        }
    }
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        k = sc.nextInt();
        n = sc.nextInt();

        choose(1);




    }
}