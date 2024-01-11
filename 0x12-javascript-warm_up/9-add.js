#!/usr/bin/node

const add = (a, b) => parseInt(a, 10) + parseInt(b, 10);

const [, , arg1, arg2] = process.argv;

if (arg1 && arg2) {
  console.log(add(arg1, arg2));
} else {
  console.log("NaN");
}

