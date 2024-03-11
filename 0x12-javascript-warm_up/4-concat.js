#!/usr/bin/node

const [arg1, arg2] = process.argv.slice(2);

if (arg1 === undefined) {
  arg1 = 'undefined';
}

if (arg2 === undefined) {
  arg2 = 'undefined';
}

console.log(`${arg1} is ${arg2}`);
