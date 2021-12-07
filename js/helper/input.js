const fs = require('fs');

function input_as_list_of_ints(file){
    return fs
        .readFileSync(file, 'utf8')
        .toString()
        .trim()
        .split('\n')
        .map((num) => parseInt(num, 10));
}

module.exports = {
    input_as_list_of_ints,
};