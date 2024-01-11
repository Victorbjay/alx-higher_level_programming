#!/usr/bin/node
exports.esrever = function (list) {
  // Reverses an array
  let len = list.length - 1;
  const newlist = [];

  for (; len >= 0; len--) {
    newlist.push(list[len]);
  }
  return newlist;
};
