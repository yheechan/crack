import numpy as np

def program_31(N,K,W,V):
  n = N
  k = K
  tlist = []

  items = list(zip(W,V))
  tlist = np.array([*items])
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