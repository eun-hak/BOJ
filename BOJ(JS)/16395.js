let [input1, input2] = require("fs")
  .readFileSync("16395.txt")
  .toString()
  .split(" ");

let dp = new Array(31).fill(1).map(() => new Array(31).fill(1));

dp[0][0] = 1;
dp[1][0] = 1;
dp[1][1] = 1;

for (let i = 1; i < 30; i++) {
  for (let j = 0; j < i; j++) {
    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1];
  }
}

console.log(dp[input1 - 1][input2 - 1]);
