import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  N, M = map(int, input().split())
  lst = list(map(int, input().split()))

  cnt = 1
  ans = -1
  while len(lst):
    maxv = max(lst)
    if M == 0 and maxv == lst[0]:
      print(cnt)
      break
    else:
      if maxv == lst[0]:
        lst = lst[1:]
        cnt += 1
      else:
        lst = lst[1:] + [lst[0]]
      M -= 1
      if M < 0:
        M = len(lst) - 1
