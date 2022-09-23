from sys import stdin
N = int(stdin.readline())

for _ in range(N):
  n, m = list(map(int,stdin.readline().split()))
  a = list(map(int,stdin.readline().split()))
  b = [0] * n
  b[m] = 1
  
  count = 0
  while True:
    if a[0] == max(a):
      count+=1
      if b[0] == 1:
        print(count)
        break
      else:
        del a[0]
        del b[0]
    else:
      a.append(a[0])
      b.append(b[0])
      del a[0]
      del b[0]