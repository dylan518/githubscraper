package Bridge;

public class Sword {
    SwordImpl realSword;

    public Sword(){
        realSword = new SwordImpl();
    }
    public Sword(SwordImpl realSword) {
        this.realSword = realSword;
    }

    double damage(){
        return realSword.damage();
    }
    double superAttack(){
        return realSword.superAttack();

    }
    void transformToFireSword(){
        realSword = new FireSword();
    }
    void transformToIceSword(){
        realSword = new IceSword();
    }

    public SwordImpl getRealSword() {
        return realSword;
    }
}
