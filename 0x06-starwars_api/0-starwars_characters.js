#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    displayActors(characters, 0);
  }
});

function displayActors (actors, index) {
  request(actors[index], function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < actors.length) {
        displayActors(actors, index + 1);
      }
    }
  });
}
