ArrayList<Morty> mortyList;
//Morty m;
float start = 2;
float end = 100;
void setup() {
  // Images must be in the "data" directory to load correctly
  size(640,320);
  for(int i = start; i < end; i += 1){
    String base = "PM"
    mortyList.add(new Morty);
  }
  m = new Morty("PM-002.png", random(0,width), random(0,height), 50, 120);
}

void draw() {
  background(127);
  m.display();
  m.moveRight();
  m.checkEdges();
}