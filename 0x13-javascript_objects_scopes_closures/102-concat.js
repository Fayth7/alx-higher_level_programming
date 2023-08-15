#!/usr/bin/node
const fs = require('fs');
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) throw err;

    const concatenatedContent = `${data1}${data2}`;

    fs.writeFile(destinationFile, concatenatedContent, 'utf8', (err) => {
      if (err) throw err;
      console.log(`Concatenated content saved to ${destinationFile}`);
    });
  });
});
