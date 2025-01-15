const input = require("fs").readFileSync("21395.txt").toString().split("\n");

// console.log(input[2].split(" ").map((num) => parseInt(num)));

for (let i = 2; i <= Number(input[0]) * 2; i += 2) {
  let num_arr = (input[i].split(" ").map((num) => parseInt(num)));

}





