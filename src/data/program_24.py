def program_24(N,K,V,W):
  def knapsack(items, limit):
      items = sorted(items, key=lambda x: x[0])                    # pre-sort
      profit = [[[0, 0], [0, 0]] for _ in range(len(items)+1)]     # length of items + 1 for the better readability
      if items[0][0] <= limit:                                     # check base case and setup starting point
          profit[1][1] = items[0]
      else:
          return 0
                                        

      for i in range(2, len(items)+1):
          pre_max = max(profit[i-1], key=lambda t: t[1])           # max of previous sub-problem
          profit[i][0] = pre_max                                   # DO NOT include itself
          profit[i][1] = pre_max                                   # DO include itself
          for w, v in items:
              if pre_max[0] + w <= limit:                          # check if current item can be added to our bag
                  profit[i][1] = max([(pre_max[0] + w, pre_max[1] + v), profit[i][1]], key= lambda x: x[1])
              else:                                                # if not, move onto next iteration
                  break
      return max(profit[-1], key=lambda x: x[1])[1]                # return optimal value

  n= N
  limit = K
  wv = []
  for i in range(n):
      wv.append([W[i],V[i]])

  return (knapsack(wv, limit))