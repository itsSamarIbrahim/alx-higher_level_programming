#!/usr/bin/node

const files = require('files');

const file1 = files.readFileSync(process.argv[2], 'UTF-8').toString();

const file2 = files.readFileSync(process.argv[3], 'UTF-8').toString();

files.writeFileSync(process.argv[4], file1 + file2);
