def program_35(N,K,V,W):
  a = N
  b = K
  dic = {}
  sum_value = []
  sum_weight = 0
  sort_arr = []

  for i in range(a):
      x, y = [W[i],V[i]]
      sort_arr.append([])
      sort_arr[i].append(x)
      sort_arr[i].append(y)
      sum_value.append(0)

  sort_arr.sort(key = lambda x:x[1], reverse=True)
  count = 0

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