def program_32(N,K,W,V):
  n = N
  k = K
  dp = [[0 for _ in range(k+1)] for _ in range(n)]

  for i in range(n):
    weight = W[i]
    value = V[i]

    if weight <= k:
      for j in range(k - weight + 1):
        dp[i][j + weight] = max(dp[i-1][j + weight], dp[i-1][j] + value)
      for j in range(weight):
        dp[i][j] = dp[i-1][j]

  return dp[n-1][k]
