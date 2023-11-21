# 물건이 하나일 때 잘못된 값 리턴
# ex)
# 1 100000
# 1 2

def program_26(N,K,V,W):

  things = zip(W,V)
  things = sorted(things, key=lambda x: x[0])
  # dp[i][j] = i번째 things까지 사용해서 j 무게를 채워 얻는 최고 가치
  dp = [[0] * (K + 1) for _ in range(N)] # 차이 부분
  for n in range(N):
      w, v = things[n]
      for k in range(1, K + 1):
          if w <= k:
              dp[n][k] = max(dp[n - 1][k - w] + v, dp[n - 1][k])
          else:
              dp[n][k] = dp[n - 1][k]

  return dp[N - 1][K]