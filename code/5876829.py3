case1 = int(input())
for x in range(case1):
  cnt = 0
  size,idx = input().split()
  size = int(size)
  idx = int(idx)
  tmp = input().split()
  n = list(map(int,tmp))

  for x in range(size):
    max_num = max(n)
    while max_num != n[0]:
      n += [ n[0]]
      n.remove(n[0])
      if idx == 0:
        idx = len(n) - 1
      else:
        idx -= 1
    if idx == 0:
      cnt += 1
      break
    else:
      n.remove(n[0])
      idx -= 1
      cnt += 1
  print(cnt)