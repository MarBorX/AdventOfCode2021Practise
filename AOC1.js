console.log("--- Day 1: Sonar Sweep ---");

// import using readFileSync and separate
const fs = require('fs');
const array = fs.readFileSync("AOC1.txt")
    .toString()
    .trim()
    .split("\n")
    .map((num) => parseInt(num,10));


// ***PART I***
// Counter for each increase
let counter = 0;

for(let i = 1; i<array.length; i++){
    // When increasing
    if(array[i] > array[i-1]){
        counter++;
    }
}

console.log(counter);

// ***PART II***
// Counter
let threeSlidingWindowIncreases = 0;
var sumArray = [];

for(let j=2; j<array.length; j++){
    sumArray.push(array[j-2] + array[j-1] + array[j-0]);
}

for(let k=1; k<sumArray.length; k++){
    if(sumArray[k] > sumArray[k-1]){
        threeSlidingWindowIncreases++;
    }
}

console.log(threeSlidingWindowIncreases);