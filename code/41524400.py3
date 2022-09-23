import sys
si = sys.stdin.readline
T = int(si())
order_list = []

for _ in range(T):
  n, m = map(int, si().split())
  imp = list(map(int, si().split()))
  idx = list(range(n))
  idx[m] = 'target'

  order = 0

  while True:
    if imp[0] >= max(imp):
      order += 1
      if idx[0] == 'target':
        order_list.append(order)
        break
      imp.pop(0)
      idx.pop(0)
    else:
      imp.append(imp.pop(0))
      idx.append(idx.pop(0))

for x in order_list:
  print(x)