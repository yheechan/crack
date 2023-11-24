import numpy as np

def program_29(N,K,W,V):
    cases = N
    bag = K
    items = list(zip(W,V))
    items = np.array([*items])
    # items = sorted(items, key=lambda x: x[0])
    d = [[0,0] for _ in range(cases)]
    for i in range(cases) :
        isAdded = False
        for j in range(i+1,len(d)) :
            if items[i][0] + d[j][0] <= bag :
                d[j][0] += items[i][0]
                d[j][1] += items[i][1]
                isAdded = True
        if isAdded :
            d.append(items[i])
    d.sort(key=lambda x : -x[1])
    return d[0][1]