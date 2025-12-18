package Fish;

import java.awt.*;

public class MyFish {
    Image img = GameUtils.MyFish_L;

    int x = 700;
    int y = 450;
    int width = 60;
    int height = 45;
    int speed = 20;

    int level = 1;

    void logic(){
        if(GameUtils.Up){
            y -= speed;
        }
        if(GameUtils.Down){
            y += speed;
        }
        if(GameUtils.Left){
            x -= speed;
            img = GameUtils.MyFish_L;
        }
        if(GameUtils.Right){
            x += speed;
            img = GameUtils.MyFish_R;
        }
    }   

    public void paintSelf(Graphics g){
        logic();
        g.drawImage(img, x, y, width + GameUtils.count, height + GameUtils.count, null);
    }
    
    public Rectangle getRect(){
        return new Rectangle(x, y, width + GameUtils.count, height + GameUtils.count);
    }
}
