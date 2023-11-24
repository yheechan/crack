import heapq

def program_11(N: int, B: int, W: list, V: list) -> int:
    class T:
        def __init__(self, weight_sum, value_sum, index):
            self.weight_sum = weight_sum
            self.value_sum = value_sum
            self.index = index

        def __lt__(self, other):
            if self.weight_sum == other.weight_sum:
                return self.value_sum > other.value_sum
            else:
                return self.weight_sum < other.weight_sum

    def in_bag(n, w_max):
        global high
        q = []
        ret = 0

        for i in range(n):
            heapq.heappush(q, T(wv[i][0], wv[i][1], i))

            while q:
                current = heapq.heappop(q)
                w_sum, v_sum, b_idx = current.weight_sum, current.value_sum, current.index

                if high[w_sum] > v_sum:
                    continue

                for j in range(b_idx + 1, n):
                    bag_w, bag_v = wv[j][0], wv[j][1]

                    if bag_w + w_sum > w_max:
                        break

                    if high[bag_w + w_sum] < bag_v + v_sum:
                        heapq.heappush(q, T(bag_w + w_sum, bag_v + v_sum, j))
                        high[bag_w + w_sum] = bag_v + v_sum

        for i in range(w_max + 1):
            if high[i] > ret:
                ret = high[i]

        return ret

    global high
    high = [0] * 10000001
    wv = [(W[i], V[i]) for i in range(N)]
    bag = [[0] * (B + 1) for _ in range(N + 1)]
    ans = in_bag(N, B)

    return ans