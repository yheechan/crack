def program_16(N: int, B: int, W: list, V: list) -> int:
    selected = [False] * (N + 1)
    memo = [0] * (B + 1)

    def checknode(index, weight, value):
        nonlocal memo

        if memo[weight] != 0:
            return memo[weight]

        for i in range(index, N):
            if selected[i]:
                continue

            nextWeight = weight + W[i]
            if nextWeight > B:
                continue

            nextValue = value + V[i]

            selected[i] = True
            memo[weight] = max(memo[weight], nextValue)
            memo[weight] = max(memo[weight], checknode(i, nextWeight, nextValue))
            selected[i] = False

        return memo[weight]

    return checknode(0, 0, 0)