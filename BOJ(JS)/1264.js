let input = require("fs").readFileSync('/dev/stdin').toString().split("\n");

for (let ans of input) {
  const Vowel = ["a", "e", "i", "o", "u"];
  if (ans === "#") {
    break;
  }
  let answer = 0;
  for (let i of ans) {
    if (Vowel.includes(i.toLowerCase())) {
      answer += 1;
    }
  }
  console.log(answer);
}
