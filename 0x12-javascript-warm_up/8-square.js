#!/usr/bin/node

const SIZE = process.argv[2];

if (!Number.isInteger(parseInt(SIZE))) {
  console.log('Missing size');
} else {
  const SQUARE_SIZE = parseInt(SIZE);

  for (let i = 0; i < SQUARE_SIZE; i++) {
    let row = '';
    for (let j = 0; j < SQUARE_SIZE; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
