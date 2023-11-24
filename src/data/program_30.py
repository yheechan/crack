def program_30(N,K,weight,value):
  best_VALUE_by_K = [0] * (K+1)
  for i in range(N):
    W = weight[i]
    V = value[i]
    if i == 0:
      if W <= K:
        best_VALUE_by_K[W] = V
    else:
      change_flag = [0] * (K+1)
      for j in range(K+1):
        if (j+W) <= K:
            if j > 0 and best_VALUE_by_K[j] != 0 and change_flag[j] != 1 and (best_VALUE_by_K[j] + V) > best_VALUE_by_K[j+W]:
              best_VALUE_by_K[j+W] = best_VALUE_by_K[j] + V
              change_flag[j + W] = 1
            elif j == 0:
              if V > best_VALUE_by_K[W]:
                best_VALUE_by_K[W] = V
                change_flag[W] = 1

  return max(best_VALUE_by_K)