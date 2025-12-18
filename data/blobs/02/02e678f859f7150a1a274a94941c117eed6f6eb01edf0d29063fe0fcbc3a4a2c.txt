import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class HitAndBlow {
    public static void main(String[] args) {
        ArrayList<Integer> comList = new ArrayList<>();
        String[] userList = {};
        Scanner scanner = new Scanner(System.in);
        int i = 0;//while文の回転回数カウント用

        
        comList = addList();
        System.out.println(comList);

        // 数字を当てる処理
        while (true) {
            int blowCount = 0;
            int hitCount = 0;
            System.out.println("四桁の数字を入力してください:");

            String userInput = scanner.next();//処理の都合上必ずここで4桁入ってくる
            userList = userInput.split("");

            if(Integer.parseInt(userList[i]) == comList.get(i)){
                blowCount++;
            }

            for(int j = 0;j<userList.length;j++){
                if(Integer.parseInt(userList[j]) == comList.get(j)){
                    hitCount++;
                }
            }

            if(hitCount == 4){
                System.out.println("おめでとう！"+(i+1)+"回目で成功！");
                return;
            }

            // if(Integer.parseInt(userInput) == countNumber){
            //     hitCount++;
            // }
            System.out.println("ヒット："+hitCount+"個、ブロー："+blowCount+"個");
            //while文の一番最後の処理
            i++;
        }

    }

    public static int numGanerator(){
        Random rand = new Random();
        int num = rand.nextInt(9);

        return num;
    }

    public static ArrayList<Integer> addList(){
        int num = numGanerator();

        ArrayList<Integer> list = new ArrayList<>();

        list.add(num);

        //comListに数字が重ならないよう追加していく処理
        while (true) {
            
            int i=0;
            
            if(!(list.get(i) == num)){
                list.add(num);
            }
            if(list.size() == 4){
                break;
            }
            num = numGanerator();
            i++;
        }
        return(list);
    }
}
