import greenfoot.*;
public class HealthBar extends Actor
{
    GreenfootImage ally = new GreenfootImage("HealthBarAlly.png");
    GreenfootImage enemy = new GreenfootImage("HealthBarEnemy.png");
    Troop troop;
    Tower tower;
    boolean isAlly;
    int baseHP;
    double percentage;
    public HealthBar(Troop troop, boolean isAlly)
    {
        this.troop = troop;
        this.isAlly = isAlly;
        this.baseHP = troop.hp;
        if(isAlly)
            setImage(ally);
        else
            setImage(enemy);
    }
    
    public HealthBar(Tower tower, boolean isAlly)
    {
        this.tower = tower;
        this.isAlly = isAlly;
        this.baseHP = tower.hp;
        if(isAlly)
            setImage(ally);
        else
            setImage(enemy);
    }
    
    public void act()
    {
        if(troop != null)
        {
            if(troop.hp > 0 && baseHP < 100)
                checkHP();
            else if(troop.hp > 0 && baseHP >= 100)
                checkBigHP();
            else
                getWorld().removeObject(this);
        }
        else
        {
            if(tower.hp > 0)
                checkTowerHP();
            else
                getWorld().removeObject(this);
        }
    }
    
    public void checkHP()
    {
        int hp = troop.hp;
        if(hp > 0)
            percentage = ((double)hp / (double)baseHP) * 100;
        
        if(percentage >= 10 && isAlly)
            ally.scale((int)percentage / 10, 3);
        if(percentage >= 10 && !isAlly)
            enemy.scale((int)percentage / 10, 3);
        
        if(hp > 0)
            setLocation(troop.getX() + ((int)percentage / 20) - 5, troop.getY() - 20);
    }
    
    public void checkBigHP()
    {
        int hp = troop.hp;
        if(hp > 0)
            percentage = ((double)hp / (double)baseHP) * 100;
        
        if(percentage >= 10 && isAlly)
            ally.scale((int)percentage / 4, 3);
        if(percentage >= 10 && !isAlly)
            enemy.scale((int)percentage / 4, 3);
        
        if(hp > 0)
            setLocation(troop.getX() + ((int)percentage / 20) - 5, troop.getY() - 20);
    }
    
    public void checkTowerHP()
    {
        int hp = tower.hp;
        if(hp > 0)
            percentage = ((double)hp / (double)baseHP) * 100;
        
        if(percentage > 10 && isAlly)
            ally.scale((int)percentage / 4, 3);
        if(percentage > 10 && !isAlly)
            enemy.scale((int)percentage / 4, 3);
        
        if(hp > 0)
            setLocation(tower.getX() - (10 - (int)percentage / 10), tower.getY() - 20);
    }
}
