/*
开放型题目，随意发挥：
	写一个类Army,代表一支军队，这个类有一个属性Weapon数组w（用来存储该军队所拥有的所有武器），
	该类还提供一个构造方法，在构造方法里通过传一个int类型的参数来限定该类所能拥有的最大武器数量,
	并用这一大小来初始化数组w。

	该类还提供一个方法addWeapon(Weapon wa),表示把参数wa所代表的武器加入到数组w中。
	在这个类中还定义两个方法attackAll()让w数组中的所有武器攻击；
	以及moveAll()让w数组中的所有可移动的武器移动。

	写一个主方法去测试以上程序。

	提示：
		Weapon是一个父类。应该有很多子武器。
		这些子武器应该有一些是可移动的，有一些
		是可攻击的。
 */
public class Homework {
    public static void main(String[] args) {
        Army army = new Army(5);
        army.addWeapon(new Weapon(true));
        army.addWeapon(new Weapon(true));
        army.addWeapon(new Weapon(false));
        army.addWeapon(new Weapon(true));
        army.addWeapon(new Weapon(false));
        army.addWeapon(new Weapon(false));

        army.attackAll();
        army.moveAll();
    }
}
class Army{
    private Weapon[] w;
    private int index;
    private int max;

    public Army(int num) {
        this.w = new Weapon[num];
        this.index = -1;
        this.max = num;
    }

    public Weapon[] getW() {
        return w;
    }

    public void setW(Weapon[] w) {
        this.w = w;
    }

    public void addWeapon(Weapon wa){
        if (index == max - 1) {
            System.out.println("已达到武器上限，无法再添加武器");
            return;
        }
        this.w[++index] = wa;
    }

    public void attackAll(){
        for (int i = 0; i < w.length; i++) {
            System.out.print("第" + (i + 1) + "号");
            w[i].fire();
        }
    }

    public void moveAll(){
        for (int i = 0; i < w.length; i++) {
            if (w[i].isStatus()) System.out.print("第" + (i + 1) + "号");
            w[i].move();
        }
    }

}
class Weapon{
    private boolean status;

    public Weapon(boolean movable) {
        this.status = movable;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public void move(){
        if (this.status == true){
            System.out.println("武器移动！");
        }
    }

    public void fire(){
        System.out.println("武器开火！");
    }
}
