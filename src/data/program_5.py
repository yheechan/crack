def program_5(N: int, B: int, W: list, V: list) -> int:
    nk = [N, B]
    wv = []
    for i in range(nk[0]):
        wwvv = [W[i], V[i]]
        wv.append((wwvv[0], wwvv[1]))
    
    bag = [[0] * (nk[1] + 1) for _ in range(nk[0] + 1)]
    ans = 0
    
    for i in range(nk[0]):
        for j in range(nk[1] + 1):
            if j + wv[i][0] <= nk[1]:
                bag[i + 1][j + wv[i][0]] = max(bag[i + 1][wv[i][0]], bag[i][j] + wv[i][1])
                ans = max(ans, bag[i + 1][j + wv[i][0]])

    return ans