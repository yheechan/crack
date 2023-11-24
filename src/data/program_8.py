from collections import deque

def program_8(N: int, B: int, W: list, V: list) -> int:
    answer = 0
    K = B
    weights = W
    values = V
    dp = [0] * (K + 1)

    for i in range(1, N + 1):
        dq_temp = deque([(weights[i - 1], values[i - 1])])

        for j in range(1, K + 1):
            if j + weights[i - 1] > K:
                break

            if dp[j] != 0:
                dq_temp.append((j + weights[i - 1], dp[j] + values[i - 1]))

        for weight, val in dq_temp:
            dp[weight] = max(dp[weight], val)

            if dp[weight] > answer:
                answer = dp[weight]

    return answer