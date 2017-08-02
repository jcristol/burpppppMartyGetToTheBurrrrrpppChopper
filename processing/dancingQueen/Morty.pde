class Morty {
  PImage img;
  float x, y, img_width, img_height;
  
  Morty(PImage img, float x, float y, float img_width, float img_height){
    this.img = img;
    this.x = x;
    this.y = y;
    this.img_width = img_width;
    this.img_height = img_height;
  }
  
  void display(){
    image(img, x,y,img_width, img_height);
  }
  
  void moveRight(){
    x = x + 1;
    y = y + random(-1,1);
  }
  
  void checkEdges(){
    if(x > width){
      x = 0;
    }
  }
}