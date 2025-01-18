function tiling(n) {
  const dp = Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;
  for (let i = 3; i <= n; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 100007;
  }

  return dp;
}

// 테스트 코드
console.log(tiling(2)); // 출력: 2
console.log(tiling(9)); // 출력: 55
console.log(tiling(100)); // 출력: ?
