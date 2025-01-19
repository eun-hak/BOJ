function maxStairScore(n, scores) {
  if (n === 1) return scores[0];
  if (n === 2) return scores[0] + scores[1];

  const dp = Array(n).fill(0);

  dp[0] = scores[0];
  dp[1] = scores[0] + scores[1];
  dp[2] = Math.max(scores[0] + scores[2], scores[1] + scores[2]);

  for (let i = 3; i < n; i++) {
    dp[i] = Math.max(
      dp[i - 2] + scores[i],
      dp[i - 3] + scores[i - 1] + scores[i],
    );
  }

  return dp[n - 1];
}

// 테스트 코드
console.log(maxStairScore(6, [10, 20, 15, 25, 10, 20])); // 출력: 75
