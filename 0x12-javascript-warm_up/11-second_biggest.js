#!/usr/bin/node

const argsList = process.argv.slice(2);
const nums = argsList.map(arg => parseInt(arg));

if (nums.length < 2) {
  console.log(0);
} else {
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
