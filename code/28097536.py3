T =int(input())

for _ in range(T):
  cnt=0
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  a_flag =[False]*n
  a_flag[m]=True
  while a:
    if a[0]==max(a):
      cnt+=1
      if a_flag[0]:
        break
      del a[0]
      del a_flag[0]
    else:
      a+=[a[0]]
      a_flag+=[a_flag[0]]
      del a[0]
      del a_flag[0]
  print(cnt)
