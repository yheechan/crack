def program_19(N: int, B: int, W: list, V: list) -> int:
    K = B
    item_list = [[W[i], V[i]] for i in range(N)]
    item_list.sort()

    dp = [[0, 0] for i in range(N)] # [weight_sum, value_sum]

    for i in range(N):
        if item_list[i][0] <= K:
            dp[i][0] = item_list[i][0]
            dp[i][1] = item_list[i][1]
            for j in range(N):
                if j != i:
                    if dp[i][0] + item_list[j][0] <= K:
                        dp[i][0] += item_list[j][0]
                        dp[i][1] += item_list[j][1] 
        else:
            continue
                    
    result_dp = [dp[i][1] for i in range(N)]
    return max(result_dp)