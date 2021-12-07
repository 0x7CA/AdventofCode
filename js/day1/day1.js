const { input_as_list_of_ints } = require('../helper/input.js');
const path = require('path');

const input = input_as_list_of_ints(path.join(__dirname, './input.txt'));

function calculateIncreases(arr, window = 1){
    let a = arr.slice();
    let b = arr.slice(window,);

    let increases = [];
    for (let idx of [...b.keys()]){
        increases.push(b[idx] > a[idx]);
    }
    return increases
}

const increases = calculateIncreases(input);
console.log(`Part 1 solution: ${increases.reduce((a, b) => a + b, 0)}`)
const increases2 = calculateIncreases(input, 3);
console.log(`Part 2 solution: ${increases2.reduce((a, b) => a + b, 0)}`)
