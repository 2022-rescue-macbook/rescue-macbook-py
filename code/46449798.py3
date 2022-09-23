import sys

count = int(sys.stdin.readline())
for _ in range(count):
  n, m = map(int, sys.stdin.readline().split())
  importance = list(map(int, sys.stdin.readline().split()))
  idx = list(range(len(importance)))

  order = 0
  idx[m] = 'check'
  while True:
    if importance[0] == max(importance):
        order += 1
        if idx[0] == 'check':
            print(order)
            break
        else:
            importance.pop(0)
            idx.pop(0)
    else:
        importance.append(importance.pop(0))
        idx.append(idx.pop(0))
