package jd_tasks_13;
//Create a class named 'StateClients':
//   - Create multiple objects representing different states.
//   - Test the methods and variables of each object.
public class StateClients {
    public static void main(String[] args) {

        Virginia virginia = new Virginia("Virginia", "VA", "Pepublican", "Glenn Youngkin","Tim Kaine", 8_715_698);
        California california = new California("California", "CA","Democratic", "Gavin Newsom", "Laphonza Butler", 38_965_193);
        Texas texas = new Texas("Texas", "TX", "Republican", "Greg Abbott", "Ted Cruz", 30_503_301);
        Florida florida = new Florida("Florida", "FL", "Republican", "Ron DeSantis","Rick Scott", 22_610_726);

        System.out.println(virginia);
        System.out.println(california);
        System.out.println(texas);
        System.out.println(florida);
    }
}
