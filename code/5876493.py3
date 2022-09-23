for i in range(int(input())):
  que = []; page, want = map(int, input().split()); count = 0
  po = list(map(int, input().split()))
  for j in range(page):
    que.insert(0, (j, po[j]))
  while True:
    if que[-1][1] != max(po): que.insert(0,que.pop())
    else:
      if que[-1][0] == want:
        count += 1; break
      else: que.pop(); po.remove(max(po)); count += 1
  print(count)