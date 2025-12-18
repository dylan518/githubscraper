//Carter Arribas
// Chest and Back Class
// Dedicated to running the main operations of the Chest and Back Class
// 26 Novemeber 2024





package com.processing_example;

import processing.core.PApplet;
import processing.core.PImage;

public class ChestAndBack extends DiagramScreens{
  //Head Button Placement for Hover
  float scapulaButtonX = 1025;
  float scapulaButtonY = 700;
 
  //Chest Button Placement for Hover
  float ribButtonX = 600;
  float ribButtonY = 770;

  //Arm Button Placement for Hover
  float thoracicSpineButtonX = 825;
  float thoracicSpineButtonY = 900;

  float buttonRadius = 10;
  PApplet parent;
  PImage chestAndBack;

  Scapula scapula;
  RibCage ribCage;
  ThoracicSpine thoracicSpine;


    ChestAndBack(PApplet parent){
        super(parent);
        this.parent = parent;
        chestAndBack = parent.loadImage("chestAndBack.jpg");
    }
public void draw(){
    parent.background(255);
    parent.image(chestAndBack, 450, 400, 750, 750);
    drawScapulaButton();
    drawRibButton();
    drawSpineButton();
    displayChestAndBack();

}

public void setup(){
    scapula = new Scapula(parent);
    ribCage = new RibCage(parent);
    thoracicSpine = new ThoracicSpine(parent);
    }

//Function for drawing Scapula button
public void drawScapulaButton(){
    parent.fill(65, 105, 225); // Button color
    parent.noStroke();
    parent.ellipse(scapulaButtonX, scapulaButtonY, buttonRadius * 2, buttonRadius * 2);
}

//Function for drawing Rib button
public void drawRibButton(){
    parent.fill(65, 105, 225); // Button color
    parent.noStroke();
    parent.ellipse(ribButtonX, ribButtonY, buttonRadius * 2, buttonRadius * 2);
}

//Function for drawing Spine button
public void drawSpineButton(){
    parent.fill(65, 105, 225); // Button color
    parent.noStroke();
    parent.ellipse(thoracicSpineButtonX, thoracicSpineButtonY, buttonRadius * 2, buttonRadius * 2);
}

//Check if the mouse is over the fucntion
public boolean isMouseOverBackButton() {
    return parent.mouseX >= 10 && parent.mouseX <= 90 &&
        parent.mouseY >= 10 && parent.mouseY <= 40;
}

//Hover Functions to determine if the mouse is over the desired area
boolean isMouseOverButton(float buttonX, float buttonY, float buttonRadius) {
    float distance = parent.dist(parent.mouseX, parent.mouseY, buttonX, buttonY);
    return distance <= buttonRadius;
}


public void displayChestAndBack(){
    if (isMouseOverButton(scapulaButtonX, scapulaButtonY, buttonRadius)) {
        scapula.displayInfo();
        }  
    if (isMouseOverButton(ribButtonX, ribButtonY, buttonRadius)) {
        ribCage.displayInfo();
        }
    if (isMouseOverButton(thoracicSpineButtonX, thoracicSpineButtonY, buttonRadius)) {
         thoracicSpine.displayInfo();
        }      
}

}//End Chest And Back Class