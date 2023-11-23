def program_15(N: int, B: int, W: list, V: list) -> int:
    n, k = N, B
    a = [[W[i], V[i]] for i in range(n)]

    temp3 = 0
    for w in range(n):
        for t in range(1, n - w):
            temp = a[w][0] + a[w + t][0]  # 무게
            temp2 = a[w][1] + a[w + t][1]  # 가치
            if temp <= k:
                if temp2 > temp3:
                    temp3 = temp2

    return temp3
