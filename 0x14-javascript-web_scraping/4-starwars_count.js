#!/usr/bin/node
/* a script that prints the number of movies where the character
“Wedge Antilles” is present */
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const data = JSON.parse(body);

  const wedgeId = '18';

  const wedgeMoivesCount = data.results.filter(moive => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}`)).length;

  console.log(wedgeMoivesCount);
});
