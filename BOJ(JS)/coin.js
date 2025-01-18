let fs = require('fs');
let input = fs.readFileSync('coin.txt').toString().split('\n');

let coinSum = parseInt(input[0].split(' ')[1]);

let coinArr = [];
let answer = 0;
for (let i = 1; i < input.length; i++) {
  coinArr.push(parseInt(input[i]));
}
let SortedCoinArr = coinArr.sort((a, b) => b - a);

for (i of SortedCoinArr) {
  if (parseInt(coinSum / i) > 0) {
    sum = parseInt(coinSum / i);
    answer += sum;
    coinSum -= i * sum;
  }
}
console.log(answer);
