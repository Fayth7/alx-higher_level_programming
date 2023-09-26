#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    const characterPromises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const charData = JSON.parse(charBody);
            resolve(charData.name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      })
      .catch((err) => {
        console.error(err);
      });
  }
});
