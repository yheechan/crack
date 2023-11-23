def program_7(N: int, B: int, W: list, V: list) -> int:
    arr = []
    dp = []
    temp = [0, 0]

    for i in range(N):
        arr.append([W[i], V[i]])
        dp.append([arr[i][0], arr[i][1]])

    def package(p, temp):
        if p == N:
            return

        if temp[0] + arr[p][0] > B:
            return

        if temp[0] + arr[p][0] <= B:
            temp[0] += arr[p][0]
            temp[1] += arr[p][1]
            package(p + 1, temp)

    for i in range(N):
        if arr[i][0] > B:
            dp[i][1] = 0
            continue

        temp = [arr[i][0], arr[i][1]]
        package(i + 1, temp)
        dp[i][1] = max(dp[i][1], temp[1])

    t = 0
    for i in range(N):
        t = max(t, dp[i][1])

    return t