#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, reponse, body) => {
  if (error) {
    console.log('Error: ' + error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  characters.forEach(character => {
    request(character, (error2, response2, body2) => {
      if (error2) {
        console.log('Error: ' + error2);
      }
      const person = JSON.parse(body2);
      console.log(person.name);
    });
  });
});
