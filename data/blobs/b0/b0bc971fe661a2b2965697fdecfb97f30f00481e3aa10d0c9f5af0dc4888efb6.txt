import java.util.Scanner;

public class Account {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int result_price;  //전체 가격
        int all_count; //전체 구매종류 갯수

        int item_price;  //구매품목 가격
        int item_count;  //구매품목 갯수

        int result_price2 = 0;

        result_price = sc.nextInt();

        all_count = sc.nextInt();

        for(int i = 0; i < all_count; i++){
            item_price = sc.nextInt();
            item_count = sc.nextInt();
            result_price2 += item_price*item_count;
        }

        if(result_price2 == result_price){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
