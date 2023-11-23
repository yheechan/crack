def program_9(N: int, B: int, W: list, V: list) -> int:
    MAX_N = 10**5 + 5

    xx = [1, 0, -1, 0]
    yy = [0, 1, 0, -1]

    M = B
    arr = [[0] * MAX_N for _ in range(105)]

    inp = []
    for i in range(1, N + 1):
        inp.append((W[i - 1], V[i - 1]))

    for i in range(1, N + 1):
        wei, val = inp[i - 1]
        for j in range(1, M + 1):
            if wei <= j:
                arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - wei] + val)
            else:
                arr[i][j] = arr[i - 1][j]

    return arr[N][M]
