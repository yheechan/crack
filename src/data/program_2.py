def compare(a, b):
    return a[0] < b[0]

def program_2(N: int, B: int, W: list, V: list) -> int:
    K = B

    A = [(0, 0)] * (N + 1)
    for i in range(1, N + 1):
        A[i] = (W[i - 1], V[i - 1])

    A.sort(key=lambda x: x[0])  # 오름차순 정렬

    DP = [[0] * (K + 1) for _ in range(N + 1)]  # DP 배열 0으로 초기화

    for i in range(1, N + 1):
        border = min(K, 2 * A[i][0] - 1)  # 하나의 물건이 중복해서 담기지 않도록 한계 설정
        for j in range(1, border + 1):
            if A[i][0] <= j:
                DP[i][j] = max(DP[i][j - A[i][0]] + A[i][1], DP[i - 1][j])
            else:
                DP[i][j] = DP[i - 1][j]

        for j in range(border + 1, K + 1):  # 한계점 이후로 코드
            DP[i][j] = max(DP[i][border], DP[i - 1][j - A[i][0]] + A[i][1])

    M = 0

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            M = max(DP[i][j], M)  # 최대값 찾기

    return M
