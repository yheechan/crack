import heapq

def program_20(N: int, B: int, W: list, V: list) -> int:
    nk = [N, B]
    wv = []
    for i in range(nk[0]):
        wwvv = [W[i], V[i]]
        wv.append((wwvv[0], wwvv[1]))
    
    high = [0] * (nk[1] + 1)
    bag = []

    class T:
        def __init__(self, weight_sum, value_sum, index):
            self.weight_sum = weight_sum
            self.value_sum = value_sum
            self.index = index

    # 무게 합 오름차순 이후 가치 합 내림차순 정렬
    class Qcompare:
        def __lt__(self, t1, t2):
            if t1.weight_sum == t2.weight_sum:
                return t1.value_sum > t2.value_sum
            else:
                return t1.weight_sum < t2.weight_sum

    # 무게 오름차순 이후 가치 내림차순 정렬
    def Vcompare(a, b):
        if a[0] == b[0]:
            return a[1] > b[1]
        else:
            return a[0] < b[0]

    def inBag(n, wMax):
        ret = 0
        q = []

        for i in range(n):
            heapq.heappush(q, T(bag[i][0], bag[i][1], i))

            while q:
                t = heapq.heappop(q)
                w_sum = t.weight_sum
                v_sum = t.value_sum
                b_idx = t.index

                if high[w_sum] > v_sum:
                    continue

                # b_idx 이후 부터 검사
                for j in range(b_idx + 1, n):
                    bag_w = bag[j][0]
                    bag_v = bag[j][1]

                    if bag_w + w_sum > wMax:
                        break
                    if high[bag_w + w_sum] < bag_v + v_sum:
                        heapq.heappush(q, T(bag_w + w_sum, bag_v + v_sum, j))
                        high[bag_w + w_sum] = bag_v + v_sum

        for i in range(wMax + 1):
            if high[i] > ret:
                ret = high[i]

        return ret

    for i in range(N):
        bag.append((W[i], V[i]))

    bag.sort(key=lambda x: (x[0], -x[1]))

    return inBag(N, B)
