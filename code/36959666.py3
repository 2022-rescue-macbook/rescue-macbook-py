test_case=int(input())

for _ in range(test_case):
  n,m=map(int, input().split())
  s=list(map(int, input().split()))
  idx=[0 for _ in range(n)]

  idx[m]=1
  cnt=0
  while True:
    if s[0]==max(s):
      cnt+=1
      if idx[0]==1:
        print(cnt)
        break
      else:
        del s[0]
        del idx[0]
    else:
      s.append(s[0])
      del s[0]
      idx.append(idx[0])
      del idx[0] 