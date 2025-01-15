const input = require("fs").readFileSync("10828.txt").toString().split("\n");

const iter = input.shift();

let stack = [];

// 시간 초과되는 것을 방지하기 위해
// ans 배열에 값들을 넣어놓고 마지막에 join으로 문자열로 바꿔서 한번에 출력
let ans = [];

// input 배열의 원소를 하나씩 짚으면서 명령어 판단
for (let i = 0; i < iter; i++) {
  if (input[i].includes("push")) {
    // "push 1", 이런 식으로 되어있기 때문에 split을 통해 정수를 분리해야함
    let pushNum = input[i].split(" ");
    stack.push(Number(pushNum[1]));
  } else if (input[i].includes("pop")) {
    // stack.length가 0보다 커야지 pop 가능
    // 스택 가장 위(stack 배열 가장 뒤)의 정수를 빼고, 출력해야함.
    if (stack.length > 0) {
      let popNum = stack.pop();
      ans.push(popNum);
    } else {
      ans.push(-1);
    }
  } else if (input[i].includes("size")) {
    // 단순 stack.length 출력
    ans.push(stack.length);
  } else if (input[i].includes("empty")) {
    // 비어있으면 1, 들어있으면 0 출력
    if (stack.length === 0) {
      ans.push(1);
    } else {
      ans.push(0);
    }
  } else if (input[i].includes("top")) {
    // 비어있으면 -1, 들어있으면 가장 뒤에 있는 값 출력
    if (stack.length === 0) {
      ans.push(-1);
    } else {
      ans.push(stack[stack.length - 1]);
    }
  }
}

console.log(ans.join("\n"));
