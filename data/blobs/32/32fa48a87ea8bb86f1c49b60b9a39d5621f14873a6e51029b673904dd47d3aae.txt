package hwweek;

/*4. Write if else condition and print your group name in console else others group name.*/
public class Question4 {

    static String groupname = "My group name is Restassured";
    static String[] othergroup = {"Java", "Code1", "Code2", "Agile"};

    public static void main(String[] args) {

        if (groupname.equals("My group name is Restassured")) {
            System.out.println(groupname);
        } else {
            System.out.println(othergroup);
        }

    }
}