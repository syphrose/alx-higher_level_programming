#!/usr/bin/node

const callMeMoby = (x, theFunc) => {
  if (x > 0) {
    theFunc();
    callMeMoby(x - 1, theFunc);
  }
};
module.exports.callMeMoby = callMeMoby;
