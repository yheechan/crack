def program_4(N: int, B: int, W: list, V: list) -> int:
    K = B

    things = []
    for i in range(N):
        things.append((W[i], V[i]))

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