def program_22(N,K,V,W):
    n = N
    capacity = K
    weights = W
    values = V
    dp = [[0] * (capacity + 1) for _ in range(n)]

    for i in range(n):
        for w in range(capacity + 1):
            if weights[i] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i]] + values[i])  # Incorrect initialization of dp