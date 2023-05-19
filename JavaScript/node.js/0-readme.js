#!/usr/bin/node
const fs = require('fs');
const path = require('path');
import { argv } from 'node:process';

const len = argv.len;
if (len < 2) {
  console.log(`Usage: ${process.argv0}`);
} else {
  path = argv[1];
  fs.readFile(path, (err, data) => {
    if (err) console.log('Error', err);
    else console.log('Result', data);
  });
}