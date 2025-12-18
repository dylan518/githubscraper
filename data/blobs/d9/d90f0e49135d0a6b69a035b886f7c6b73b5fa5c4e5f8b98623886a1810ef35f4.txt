package JavaTrning;

public class Lop {


    public class LoopExample {
        public void main(String[] args) {
            for (int i = 0; i < 10; i++) {
                if (i == 5) {
                    System.out.println("num found ");
                    break;
                }

            }
            for (int num = 0; num < 10; num++) {
                int res = num * num;
                if (res > 40) {
                    System.out.println("the result of action is nore that 40");
                }

            }
            Boolean isPassTrue = true;
            Boolean isPassFalse = true;

// case of true
            if (isPassTrue){
                System.out.println("the value of is Pass is true ");
            }

            // case of false
            if (!isPassFalse){
                System.out.println("the value of is Pass is true ");
            }
        }
    }
}
