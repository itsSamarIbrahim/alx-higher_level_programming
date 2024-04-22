#!/usr/bin/node

const ARGS = process.argv.slice(2).map(Number);
const SORTED_ARGS = ARGS.sort((a, b) => b - a);

if (SORTED_ARGS.length <= 1) {
  console.log(0);
} else {
  console.log(SORTED_ARGS[1]);
}
