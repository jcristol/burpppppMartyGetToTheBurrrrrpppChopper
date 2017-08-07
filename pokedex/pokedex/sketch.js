// sketch.js

// var cnv;
var leftBuffer;
var rightBuffer;

function setup() {
  createCanvas(1200, 900);
  leftBuffer = createGraphics(675, 900);
  rightBuffer = createGraphics(525, 900);
  // centerCanvas();
}

function draw() {
    // Draw on your buffers however you like
    drawLeftBuffer();
    drawRightBuffer();
    // Paint the off-screen buffers onto the main canvas
    image(leftBuffer, 0, 0);
    image(rightBuffer, 675, 0);
}

function drawLeftBuffer() {
    leftBuffer.background(0, 0, 0);
    leftBuffer.fill(255, 255, 255);
}

function drawRightBuffer() {
    rightBuffer.background(255, 100, 255);
    rightBuffer.fill(0, 0, 0);
}
//
// function centerCanvas() {
//   var x = (windowWidth - width) / 2;
//   var y = (windowHeight - height) / 2;
//   cnv.position(x, y);
// }
//
// function windowResized() {
//   centerCanvas();
// }
