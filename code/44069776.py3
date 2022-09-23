T = int(input())
for i in range(0, T) :
  N, M = map(int, input().split())
  cnt = 1
  end = False
  que = list(map(int, input().split()))
  oque = list(range(0, N))
  ma = sorted(que, reverse = True)
  while not end :
    while 1 :
      x = que.pop(0)
      ox = oque.pop(0)
      if x == ma[0] :
        if ox == M :
          print(cnt)
          end = True
          break
        else :
          cnt += 1
          ma.pop(0)  
      else :
        que.append(x)
        oque.append(ox)