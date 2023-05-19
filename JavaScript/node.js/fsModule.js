#!/usr/bin/node
const fs = require('fs');

let files = fs.readdirSync('./');
console.log(files);

/* This method reads the directory */
fs.readdir('./', function(err, files) {
    if (err) console.log('Error', err);
    else console.log('Result', files);
});