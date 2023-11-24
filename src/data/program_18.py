def program_18(N: int, B: int, W: list, V: list) -> int:
    a,b=N,B
    s =[]
    for i in range(a):
        c,d = W[i], V[i]
        s.append([d/c,d,c])
    s.sort(reverse =True)
    dp= [[0 ,0]for i in range(a)]
    for i in range(a):
        for j in range(i,a):
            if dp[i][1] +s[j][2] <=b:
                dp[i][0] =max(dp[j][0],dp[i][0]+s[j][1])
                dp[i][1] = dp[i][1] +s[j][2]
    return max(dp)[0]