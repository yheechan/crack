import heapq

def program_27(N,K,W,V):
    heap_list =[]
    result =[]

    for i in range(N):
        heapq.heappush(heap_list, (-W[i], V[i]))

    for i in range(len(heap_list)):
        new_w, new_v = heapq.heappop(heap_list)
        weight =-new_w
        value =new_v
        if len(heap_list) ==0 & weight <=K:
            heapq.heappush(result, -value)
            break
        elif len(heap_list) ==0 & weight >K:
            break

        for j in range(len(heap_list)):
            if weight - heap_list[j][0] <=K:
                weight =weight - heap_list[j][0]
                value +=heap_list[j][1]
                heapq.heappush(result, -value)
    return -heapq.heappop(result)