def program_33(N,K,V,W):
  n = N
  k = K

  tlist = []

  for h in range(n):
    tlist.append([W[h],V[h]])

  maxv = 0

  for i in range(n):
      w = 0
      v = 0
      if k >= w+tlist[i][0]:
        w = w+tlist[i][0]
        v = v+tlist[i][1]
      for j in range(n-1):
        if k >= w+tlist[j+1][0]:
          w = w+tlist[j+1][0]
          v = v+tlist[j+1][1]
      if v>maxv:
        maxv = v
  return maxv