function generatePermutations(arr) {
  const result = [];
  const used = Array(arr.length).fill(false);

  function backtrack(path) {
    if (path.length === arr.length) {
      result.push([...path]);
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.push(arr[i]);
      backtrack(path);

      used[i] = false;
      path.pop();
    }
  }

  backtrack([]);
  return result;
}

// 테스트 코드
console.log(generatePermutations([1, 2, 3]));
// 출력 예시 (순서가 달라도 무관):
// [
//   [1, 2, 3],
//   [1, 3, 2],
//   [2, 1, 3],
//   [2, 3, 1],
//   [3, 1, 2],
//   [3, 2, 1]
// ]

console.log(generatePermutations([1, 1, 2]));
// 출력 예시:
// [
//   [1, 1, 2],
//   [1, 2, 1],
//   [2, 1, 1]
// ]
