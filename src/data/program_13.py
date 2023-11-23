def program_13(N: int, B: int, w: list, v: list) -> int:
    K = B
    llist = []
    sum = 0
    EV = 0
    EV_list = []
    for i in range(N):
        W,V = w[i], v[i]
        llist.append([W,V])
    for i in range(len(llist)):
        sum = 0
        EV_list.append(EV)
        EV = 0
        for j in range(i,len(llist)):
            sum += llist[j][0]
            if sum > K:
                sum -= llist[j][0]
                continue
            EV += llist[j][1]
    EV_list.sort()
    return EV_list[-1]