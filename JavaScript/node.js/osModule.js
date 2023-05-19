#!/usr/bin/node
const os = require('os');

let hostname = os.hostname;
let totalMemory = os.totalmem();
let freeMemory = os.freemem();


console.log(`Hostname: ${hostname}`);
console.log(`Total Memory: ${totalMemory}`);
console.log(`Free Memory: ${freeMemory}`);