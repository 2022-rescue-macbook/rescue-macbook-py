import sys
input = sys.stdin.readline
from collections import deque
t = int(input())


for _ in range(t):
  n,m = map(int,input().split())
  q = deque(map(int,input().split()))
  s = sorted(q)
  cnt = 1
  while True:
    if q[0] != s[-1]:
      q.append(q.popleft())
      if not m:
        m = len(q) - 1 
      else:
        m -= 1
      continue
    if not m:
      print(cnt)
      break
    s.pop()
    q.popleft()
    cnt += 1
    m -= 1
    