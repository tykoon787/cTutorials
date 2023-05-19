#!/usr/bin/node
const path = require('path');

let pathObj = path.parse(__filename);
console.log(__filename); // Path of the module itself
console.log(pathObj);