def program_23(N,K,V,W):
  n = N
  m = K
  things = [[W[i],V[i]]for i in range(n)]
  # 해당 무게에 대한 가장 높은 가치 저장
  comb = {0: 0} 

  def backpack(weight, value, idx):
      weight += things[idx][0]
      value += things[idx][1]
      if weight > m:
          return
      
      # 등록된 무게의 최고가치보다 가치가 낮으면 리턴
      if weight not in comb:
          comb[weight] = value
      elif value < comb[weight]:
          return
      else:
          comb[weight] = value
      # ex) 4까지 탐색했으면 5부터 모두 재귀호출
      for i in range(idx+1, n):
          backpack(weight, value, i)

  # 모든 물건에 대해 탐색
  for i in range(n):
      backpack(0, 0, i)

  # 가장 높은 가치 출력
  return max(comb.values())