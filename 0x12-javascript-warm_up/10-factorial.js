#!/usr/bin/node

const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

const [, , arg] = process.argv;
const result = factorial(parseInt(arg, 10));
console.log(result);

