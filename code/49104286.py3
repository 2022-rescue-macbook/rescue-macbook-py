from sys import stdin
T =int(stdin.readline())
for _ in range(T):
  N, M = map(int, stdin.readline().split())
  s = list(map(int, stdin.readline().split()))
  s_ = [0 for i in range(N)]
  s_[M] = 1
  cnt = 0
  while True:
    if s[0] == max(s):
      cnt += 1
      if s_[0] == 1:
        print(cnt)
        break
      else:
        del s[0]
        del s_[0]
    else:
      s.append(s[0])
      del s[0]
      s_.append(s_[0])
      del s_[0]