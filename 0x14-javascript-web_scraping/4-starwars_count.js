#!/usr/bin/node
/* a script that prints the number of movies where the character
“Wedge Antilles” is present */
const request = require('request');

const apiUrl = process.argv[2];

let count = 0;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const data = JSON.parse(body);

  for (const movie of data.results) {
    for (const line of movie.characters) {
      if (line.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
