#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Prints a rectangle with Xs
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    // Swaps the width with the height
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Multiplies both width and height by 2
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
