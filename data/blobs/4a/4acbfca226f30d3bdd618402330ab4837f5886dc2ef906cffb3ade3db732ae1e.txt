package family_money_management;

public class family_money_management {
    public static void main(String[] args) {
        boolean isFlag = true;
        String details = ""; //use for each money recorde
        int balance=10000;   //have money at first
        int money;           //each money earn/spend
        String info;         //money info
        while (isFlag) {
            System.out.println("\n\n_______________family money management_________________");
            System.out.println("             1.money look");
            System.out.println("             2.earn money");
            System.out.println("             3.spend money");
            System.out.println("             4.quit");
            System.out.print("              chose 1-4:");
            char selection = Utility.readMenuSelection();
            switch (selection) {
                case '1':
                    System.out.println("___________________money status________________________");
                    System.out.println("spend or earn\t\ttotal money\t\tmoney\t\tinfo");
                    System.out.println(details);
                    System.out.println("_______________________________________________________");
                    break;
                case '2':
                    System.out.print("\tinput earn money:");
                    money = Utility.readNumber();
                    System.out.print("\tinput info:");
                    info = Utility.readString();
                    //update balance
                    balance+=money;
                    //update details
                    details += "\tearn\t\t\t\t"+balance+"\t\t "+money+"\t\t"+info+"\n";
                    System.out.println("____________________input done____________________");
                    break;
                case '3':
                    System.out.print("\tinput spend money:");
                    money = Utility.readNumber();
                    System.out.print("\tinput info:");
                    info = Utility.readString();
                    if(balance>=money){
                        //update balance
                        balance-=money;
                        //update details
                        details += "\tspend\t\t\t\t"+balance+"\t\t "+money+"\t\t"+info+"\n";
                    }else {
                        System.out.println("wrong,spend too much money!");
                    }
                    System.out.println("____________________input done____________________");
                    break;
                case '4':
                    System.out.print("\tAre you sure to quit?(Y/N):");
                    char isExit = Utility.readConfirmSelection();
                    if (isExit == 'Y') {
                        isFlag = false;
                    }
                    break;
            }
        }
    }
}
