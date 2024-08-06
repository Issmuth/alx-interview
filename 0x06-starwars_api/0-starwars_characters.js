#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function promisify (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function findName (characters) {
  const characterNames = [];
  for (const character of characters) {
    try {
      const charac = await promisify(character);
      characterNames.push(charac.name);
    } catch (error) {
      console.error('Error: ', error);
    }
  }
  return characterNames;
}

request(url, (error, reponse, body) => {
  if (error) {
    console.log('Error: ' + error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  findName(characters).then(characterNames => {
    characterNames.forEach(character => {
      console.log(character);
    });
  });
});
