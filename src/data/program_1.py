import sys

def program_1(N: int, B: int, W: list, V: list) -> int:
    n = N
    weightmax = B
    values = {0: 0}

    for i in range(n):
        temp = {}
        #이미 가방에 들어있는 아이템이 또 들어가는걸 방지하기 위해 temp 딕셔너리를 만듦
        w, v = W[i], V[i]
        for e in values:
            if e + w <= weightmax:
                try:
                    temp[e + w] = max(values[e] + v, values[e+w])
                    #values[e+w]가 이미 있을때, 기존값과 새로운 값을 비교
                except:
                    temp[e + w] = values[e] + v
                    #values[e+w]가 없으면 새로운 값을 입력
        temp2 = {k: max(temp.get(k, 0), values.get(k, 0)) for k in set(temp) | set(values)} 
        #temp와 values를 temp2로 합침
        values = temp2
        #values를 temp2로 바꿈
    
    return max(values.items())[1]