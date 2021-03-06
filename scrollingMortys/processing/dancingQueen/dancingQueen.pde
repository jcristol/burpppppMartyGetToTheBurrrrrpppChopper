ArrayList<Morty> mortys = new ArrayList<Morty>();
float num_morties = 100;
float scale = 2;
void setup() {
  // Images must be in the "data" directory to load correctly
  size(1600, 800);
  surface.setResizable(true);
  for(int i = 0; i < num_morties; i += 1){
    String path_string = "../mortys/morty" + i + ".png";
    mortys.add(new Morty(loadImage(path_string), random(0,width), random(0,height), 20*scale, 40*scale));
  }
}

void draw() {
  background(127);
  updateMortys();
}


void updateMortys(){
  for(int i = 0; i < num_morties; i += 1){
    Morty m = mortys.get(i);
    m.display();
    m.moveRight();
    m.checkEdges();
  }
}

/*
Ideas:
can do some weird morty processing data visaulization
can go into the web scrapping you did
try this out in p5
try to include audio
include a background 
make a intersting visualization such as a pokedex


presentation on the process of making a morty pokedex
- the scrape what i used to scrape
- the idea process what i made and i was a bit underwhelmed
- bring back p5 js to make this pokedex

*/