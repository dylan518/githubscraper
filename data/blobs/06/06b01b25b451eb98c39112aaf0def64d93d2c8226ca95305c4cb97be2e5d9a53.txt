package main;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

import javax.swing.JPanel;

import entity.Entity;
import entity.Player;
import object.SuperObject;
import tile.TileManager;

public class gamePanel extends JPanel implements Runnable{
    //Settings
    final int originalTileSize = 16; //32x32
    final int scale = 3;

    public final int tileSize = originalTileSize * scale; // 64x64 tile
    public final int maxScreenCol = 16;
    public final int maxScreenRow = 12;
    public final int screenWidth = tileSize * maxScreenCol; //768 pixels
    public final int screenLength = tileSize * maxScreenRow; //576 pixels
    
    public boolean updateLeader = false;
    
    //world settings
    
    public final int maxWorldCol = 64;
    public final int maxWorldRow = 36;
  
    //FPS
    int FPS = 60;
    
//   Class 
    TileManager tileM = new TileManager(this);
    keyHandler keyH = new keyHandler(this);
    Sound music = new Sound();
    Sound se = new Sound();
    public collisionChecker cChecker = new collisionChecker(this);
    public AssetSetter aSetter = new AssetSetter(this);
    public UI ui = new UI(this);
    public wordGenerator wGen = new wordGenerator(this);
    Thread gameThread;
    
    public Player player = new Player(this,keyH);
    public SuperObject obj[] = new SuperObject[30];
    DecimalFormat dFormat = new DecimalFormat("#0.00");
    
    //gamesTATE
    public int gameState;
    public final int playState = 1;
    public final int titleState = 0;
    public final int pauseState = 2;
    public int pauseCount = 0;
    public int resumeCount = 1;
    public int gameEnd = 0;
    public int difficulty;
    
    // Word 
    public String word;
    public char[] wordSet = new char[5];
    public String cL1, cL2, cL3, cL4, cL5;
    public String[] showWord = new String[] {"-","-","-","-","-"};
    File board = new File("Leaderboard.txt");
    String leader1, leader2, leader3;
   
    
    
    //set player default position.

    public gamePanel() {

      this.setPreferredSize(new Dimension(screenWidth, screenLength));
      this.setBackground(Color.black);
      this.setDoubleBuffered(true);
      this.addKeyListener(keyH);
      this.setFocusable(true);
    }
    
    public void setupGame() throws IOException {
    	
    	word = getWord();
    	wGen.wordSetter(word.toCharArray());
    	wGen.wordToImage();
    	aSetter.setObject();
    	playMusic(6);
    	gameState = titleState;
    	
		sortFile();
		display();
    	
    }

    public void startGameThread(){
      gameThread = new Thread(this);
      gameThread.start();
    }

    public void run(){
    	
    	double drawInterval = 1000000000/FPS;
    	double delta = 0;
    	long lastTime = System.nanoTime();
    	long currentTime;
    	long timer = 0;
    	int drawCount = 0;
    	
    	while(gameThread != null) { 
    		currentTime = System.nanoTime();
    		delta += (currentTime - lastTime) / drawInterval;
    		timer += (currentTime - lastTime);
    		lastTime = currentTime;
    		
    		if(delta >= 1 ) {
    			try {
					update();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
    			repaint();
    			delta--;
    			drawCount++;
    		}
    		
    		if(timer >= 1000000000) { 
    			System.out.println("FPS:"+drawCount);
    			drawCount = 0;
    			timer = 0;
    		}
    	}
    }
    
    public void update() throws IOException {
    	
    	if(gameState == playState) {
    		//player
    		player.update();
    		
    		if(gameEnd == 5) {
    			if(!updateLeader) {
    				stopMusic();
        			fileWriter();
        			sortFile();
            		display();
            		updateLeader = true;
    			}
    			
				ui.gameFinished = true;
				
				
				
				
			}
    		if(resumeCount % 2 == 0) {
	    		if(pauseCount > 0 && pauseCount % 2 == 0) {
	    			music.resume();
	    			resumeCount += 1;
	    		}
    		}
    		if(difficulty == 0 && ui.playTime > 300.00) {
    			ui.gameFinishedFail = true;
    			
    		}
    		else if(difficulty == 1 && ui.playTime > 200.00) {
    			ui.gameFinishedFail = true;
    			
    		}
    		else if(difficulty == 2 && ui.playTime >= 100.00) {
    			ui.gameFinishedFail = true;
    		
    		}
    		
    	}
    	if(gameState == pauseState) {
    		//pause state stuff
    		pauseMusic();
    	}
    		
    }
    public void paintComponent(Graphics g){
      super.paintComponent(g);
      Graphics2D g2 = (Graphics2D)g;
      
      //debug
      long drawStart = 0;
      if(keyH.checkDrawTime == true) {
      drawStart = System.nanoTime();
      }
      
      //title Screen
      if(gameState == titleState) {
    	  try {
			ui.draw(g2);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
      }
      else {
    	  tileM.draw(g2);
          //object
          for(int i = 0; i < obj.length; i++) {
        	  if(obj[i] != null) {
        		  obj[i].draw(g2, this);
        	  }
          }
          
          }
          //player
          player.draw(g2);
          
          try {
			ui.draw(g2);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
          if(keyH.checkDrawTime == true) {
          long drawEnd = System.nanoTime();
          long passed = drawEnd - drawStart;
          g2.setColor(Color.white);
          g2.drawString("Draw time: " + passed, 10, 400);
          System.out.println("Draw Time: " + passed);
          }
          g2.dispose();
      }
      
    
    public void playMusic(int i) {
    	music.setFile(i);
    	music.play();
    	music.loop();
    }
    public void stopMusic() {
    	 music.stop();
    }
    public void playSE(int i) {
    	se.setFile(i);
    	se.play();
    }
    public void pauseMusic() {
    	if(pauseCount % 2 == 0) {
    		music.resume();
    		
    	}
    	else {
    		music.pause();
    	}
    }
    public String getWord() throws FileNotFoundException {
    	Scanner scan = new Scanner(new File("dictionary.txt"));
    	int lines = scan.nextInt();
    	int chosenLine = (int)(Math.random()*lines)+1;
    	System.out.println(chosenLine);
    	for(int i = 0; i< chosenLine; i++) {
    		scan.nextLine();
    	}
    	
    	return scan.nextLine();
    }
    
    public void fileWriter() throws IOException {
    	FileWriter boardWrite = new FileWriter(board, true);
    	String time = dFormat.format(ui.playTime);
   
    	boardWrite.write(time);
    	boardWrite.write("\n");
    	boardWrite.close();
    }
    public void sortFile() throws IOException {
    	BufferedReader read = new BufferedReader(new FileReader("Leaderboard.txt"));
    	ArrayList<String> lines = new ArrayList<String>();
    	String currentLine = read.readLine();

    	while (currentLine != null)
    	{
    	       lines.add(currentLine);
    	       currentLine = read.readLine();
    	}
    	Collections.sort(lines);
    	BufferedWriter writer = new BufferedWriter(new FileWriter("LeaderSort.txt"));
    	for (String line : lines)
    	{
    	       writer.write(line);

    	       writer.newLine();
    	}
    	if (read != null)
        {
            read.close();
        }

        if(writer != null)
        {
            writer.close();
        }
    }
    public void display() throws FileNotFoundException {
    	Scanner scan = new Scanner(new File("LeaderSort.txt"));
    	leader1 = scan.nextLine();
    	leader2 = scan.nextLine();
    	leader3 = scan.nextLine();
    	scan.close();
    }
    
}





















