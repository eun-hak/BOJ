let input = require("fs").readFileSync("2480.txt").toString().split("\n");
let count = Number(input[0]);
let answerStr = "";

for (let i = 1; i <= count; i++) {
  let num = input[i].split(" ");
  answerStr += Number(num[0]) + Number(num[1]) + "\n";
}
console.log(input);
console.log(answerStr);
