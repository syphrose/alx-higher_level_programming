#!/usr/bin/node

const arg2 = process.argv[2];
const n = parseInt(arg2);

if (isNaN(n)) {
  console.log(`Missing number of occurrrences`);
} else {
  for (let a = 0; a < n; a++) {
   console.log(`C is fun`);
  }
}
