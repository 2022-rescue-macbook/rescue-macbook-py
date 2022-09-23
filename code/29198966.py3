import sys
input = sys.stdin.readline
for _ in range(int(input())):
  n, m = map(int, input().split())
  s = list(map(int, input().split()))
  t = [0]*n
  t[m] = 'target'
  cnt = 0
  while(s):
    if s[0] == max(s):
      cnt += 1
      if t[0] == 'target':
        print(cnt)
        break
      s.pop(0)
      t.pop(0)
    else:
      s.append(s.pop(0))
      t.append(t.pop(0))
   