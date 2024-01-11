#!/usr/bin/node

const [, , arg] = process.argv;
const size = parseInt(arg, 10);

if (!isNaN(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log("Missing size");
}

