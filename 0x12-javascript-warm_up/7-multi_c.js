#!/usr/bin/node

const arg2 = process.argv[2];
const x = parseInt(arg2);

if (isNaN(x)) {
  console.log('Missing number of occurrrences');
} else {
  for (let a = 0; a < x; a++) {
   console.log('C is fun');
  }
}
