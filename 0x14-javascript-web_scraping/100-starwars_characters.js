#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie */

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const movieData = JSON.parse(body);

  const characterUrls = movieData.characters;

  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
      }

      const characterData = JSON.parse(body);

      console.log(characterData.name);
    });
  });
});
