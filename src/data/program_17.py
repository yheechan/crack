import sys

def program_17(N: int, B: int, W: list, V: list) -> int:
    n, k = N, B
    dp = [[0 for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        weight, value = W[i], V[i]

        if weight <= k:
            for j in range(k - weight + 1):
                dp[i][j + weight] = max(dp[i-1][j + weight], dp[i-1][j] + value)
            for j in range(weight):
                dp[i][j] = dp[i-1][j]

    return dp[n-1][k]