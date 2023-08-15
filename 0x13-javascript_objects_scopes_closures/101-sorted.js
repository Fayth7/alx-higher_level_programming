#!/usr/bin/node
const data = require('./101-data');
const occurrencesByUserId = data.dict;

const usersByOccurrence = {};

for (const userId in occurrencesByUserId) {
  const occurrence = occurrencesByUserId[userId];

  if (!(occurrence in usersByOccurrence)) {
    usersByOccurrence[occurrence] = [];
  }

  usersByOccurrence[occurrence].push(userId);
}

console.log(usersByOccurrence);
