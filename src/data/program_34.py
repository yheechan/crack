def program_34(N,K,W,V):
  n = N
  m = K
  d = [] # 들어갈 수 있는 물건 목록
  dp = [] # dp 리스트, 최댓값 + 남은 무게

  for i in range(n):
    d.append([W[i],V[i]])
    dp.append([0,0])

  d.sort(key = lambda x:(x[1]/x[0]), reverse = True)

  if d[0][0] <= m: dp[0] = [d[0][1], m-d[0][0]]
  for i in range(1, n):
    if d[i][0] <= m:
      maxdp = [0, 0]
    else:
      continue
    for j in range(i):
      if dp[j][1] >= d[i][0] and maxdp[0] <= dp[j][0]: # 무게가 남고, dp 의 가치가 클 때
        if maxdp[0] == dp[j][0]:
          if maxdp[1] > dp[j][1]: maxdp = dp[j]
        else:
          maxdp = dp[j]
    if maxdp != [0,0]:
      dp[i] = [maxdp[0]+d[i][1], maxdp[1] - d[i][0]]
    else:
      dp[i] = [d[i][1], m - d[i][0]]

  max = 0
  for i in range(n):
    if dp[i][0] > max:
      max = dp[i][0]

  return max