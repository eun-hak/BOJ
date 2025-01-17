function sumOfNumbers(n, numbers) {
  return numbers.reduce((acc, cur) => (acc += cur), 0);
}

// 테스트 코드
console.log(sumOfNumbers(5, [1, 2, 3, 4, 5])); // 출력: 15
console.log(sumOfNumbers(3, [-1, -2, -3])); // 출력: -6
console.log(sumOfNumbers(4, [0, 100, -50, -50])); // 출력: 0
