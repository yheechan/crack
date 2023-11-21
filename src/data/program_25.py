def program_25(N,K,V,W):
    a = N
    b = K
    dic = {}
    sum_value = []
    sum_weight = 0
    sort_arr = zip(W,V)
    sort_arr = sorted(sort_arr, key=lambda x: x[0])
    count = 0


    for i in range(a):
        sum_value.append(0)

    for i in range(len(sort_arr)):
        while i != len(sort_arr):
            if sum_weight + sort_arr[i][0] <= b:
                sum_weight += sort_arr[i][0]
                sum_value[count] += sort_arr[i][1]

            if sum_weight == b:
                break

            i += 1


        sum_weight = 0
        count += 1
    return max(sum_value)