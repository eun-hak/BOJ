function findNumbers(n, a, m, b) {
  const arr = a.sort((x, y) => x - y);
  const ansArr = [];

  for (let i of b) {
    let start = 0;
    let end = arr.length - 1;
    let found = false;

    while (start <= end) {
      const mid = Math.floor((start + end) / 2);

      if (arr[mid] === i) {
        ansArr.push(1);
        found = true;
        break;
      } else if (i < arr[mid]) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }

    if (!found) {
      ansArr.push(0);
    }
  }

  return ansArr;
}

// 테스트 코드
console.log(findNumbers(5, [4, 1, 5, 2, 3], 5, [1, 3, 7, 9, 5])); // 출력: [1, 1, 0, 0, 1]
console.log(findNumbers(4, [1, 2, 3, 4], 3, [5, 1, 3])); // 출력: [0, 1, 1]
