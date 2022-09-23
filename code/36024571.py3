import sys

input=sys.stdin.readline

a = int(input())

for _ in range(a):
  n,m = map(int,input().split())
  lst = list(map(int,input().split()))
  idx = list(range(len(lst)))
  idx[m]='target'

  order=0

  while True:

    if lst[0] == max(lst):
      order+=1

      if idx[0] == 'target':
        print(order)
        break
      
      else:
        lst.pop(0)
        idx.pop(0)

    else:
      lst.append(lst.pop(0))
      idx.append(idx.pop(0))