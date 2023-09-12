#!/usr/bin/node
const addMeMaybe = (num, theFunc) => {
   num++;
   theFunc(num);
};
module.exports.addMeMaybe = addMeMaybe;
