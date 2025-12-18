package Assign1;

public class baseball {
    public static void main(String[] args)
    {
        Pitcher jb = new Pitcher();
        jb.SetName("Jim  B");
        jb.Display();
        jb.PerformThrow();
        jb.PerformCatch();
        jb.PerformBat();
        Batter pedro = new Batter();
        pedro.SetName("Pedro A");
        pedro.Display();
        pedro.PerformThrow();
        pedro.PerformCatch();
        pedro.PerformBat();
        Fielder max = new Fielder();
        max.SetName("Max M");
        max.Display();
        max.PerformThrow();
        max.PerformCatch();
        max.PerformBat();
        Catcher chris = new Catcher();
        chris.SetName("Chris S");
        chris.Display();
        chris.PerformThrow();
        chris.PerformCatch();
        chris.PerformBat();
        System.out.println("JB the pitcher is crazy and confused.");
        jb.setBatterBehavior(new BatBySwingingForContact()); //Originally  jb.SetBattingBehavior(new BatBySwingingForContact());
        jb.Display();
        jb.PerformBat();

        PinchHitter bobcat = new PinchHitter();
        bobcat.SetName("Bobcat");
        bobcat.Display();
        bobcat.PerformThrow();
        bobcat.PerformCatch();
        bobcat.PerformBat();
    }
}
