import sys
T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  arr = list(map(int, input().split()))
  pr_count = 0
  pos = [0] * N
  pos[M] = 1

  while True:
    if max(arr) == arr[0]:
      pr_count += 1
      if pos[0] == 1:
        print(pr_count)
        break
      else:
        del arr[0]
        del pos[0]
    else:
      arr.append(arr[0])
      del arr[0]
      pos.append(pos[0])
      del pos[0]  