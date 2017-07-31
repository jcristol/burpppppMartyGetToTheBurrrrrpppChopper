Morty m;

void setup(){
  size(640,360);
  PImage mortyImage = loadImage("../mortys/highEnergyBigMortys/PM-009.png");
  //m = new Morty(width/2, height/2, mortyImage);
}

void draw(){
  background(255);
  m.display();
}