#!/usr/bin/node
const request = require('request');
const { json } = require('stream/consumers');

const movieId = process.argv[2]


const url = "https://swapi-api.alx-tools.com/api/films/" + movieId;

request(url, (error, reponse, body) => {
    const data = JSON.parse(body);
    characters = data["characters"];
    characters.forEach(character => {
        request(character, (error, response2, body2) => {
            const person = JSON.parse(body2);
            console.log(person["name"]);
        });
    });
});