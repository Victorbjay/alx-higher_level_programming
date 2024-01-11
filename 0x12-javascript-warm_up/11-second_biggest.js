#!/usr/bin/node

const [, , ...args] = process.argv.map(Number);
const numbers = args.filter((arg) => !isNaN(arg));

if (numbers.length <= 1) {
  console.log(0);
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}

