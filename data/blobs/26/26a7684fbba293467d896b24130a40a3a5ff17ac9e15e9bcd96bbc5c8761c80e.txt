/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package in1007_project;

import city.cs.engine.UserView;
import city.cs.engine.World;
import java.awt.Graphics2D;
import java.awt.Image;
import javax.swing.ImageIcon;

/**
 *Generates the view of the game
 * @author Minnakan Seral
 */
public class MyView extends UserView {
    character_Main pirate ;
    private Image background;

    /**
     *
     * @param world
     * @param pirate
     * @param width
     * @param height
     */
    public MyView(World world,character_Main pirate, int width, int height) {
        super(world, width, height);
        this.pirate=pirate;
        //background = new ImageIcon("data/lvl1.png").getImage();
    }
     
    /**
     *
     * @param background
     */
    public void setbackground(Image background){
        this.background=background;
    }

    /**
     *
     * @param g
     */
    public void paintBackground(Graphics2D g) {
        this.background=background;
        g.drawImage(background,0,0,this);
    }
    
    /**
     *
     * @param pirate
     */
    public void updatePirate(character_Main pirate){
        this.pirate=pirate;
    }

    /**
     *
     * @param g
     */
    public void paintForeground(Graphics2D g){
        g.drawString("Items Collected="+pirate.itemcount,16,25f);
        
            g.drawString("Health="+pirate.health,525,25f);
    }

    }
    

