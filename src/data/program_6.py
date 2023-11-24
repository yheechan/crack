def program_6(N: int, B: int, W: list, V: list) -> int:
    nk = [N, B]
    wv = []
    for i in range(nk[0]):
        wwvv = [W[i], V[i]]
        wv.append((wwvv[0], wwvv[1]))

    dp = [[-1 for _ in range(nk[1] + 1)] for _ in range(nk[0])]
    
    def dfs(idx, weight, total_value):
        if idx == nk[0]:
            return total_value

        if dp[idx][weight] != -1:
            return dp[idx][weight]

        if weight + wv[idx][0] > nk[1]:
            dp[idx][weight] = dfs(idx + 1, weight, total_value)
        else:
            dp[idx][weight] = max(dfs(idx + 1, weight + wv[idx][0], total_value + wv[idx][1]),
                                  dfs(idx + 1, weight, total_value))

        return dp[idx][weight]

    answer = dfs(0, 0, 0)
    return answer