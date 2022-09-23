t=int(input())
for i in range(t):
 n,m=map(int,input().split())
 p=[*enumerate(map(int,input().split()))]
 c=0
 while len(p):
  t=max(p,key=lambda x:x[1])
  while p[0][1]!=t[1]:
   p.append(p.pop(0))
  c+=1
  o=p.pop(0)
  if o[0]==m:
   break
 print(c)