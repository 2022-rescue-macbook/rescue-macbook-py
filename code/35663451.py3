import sys;r=lambda:map(int,sys.stdin.readline().split())
for _ in range(*r()):
 n,m=r();p=[*r()];q=sorted(p);i=0;a=1
 while 1:
  if p[i]==q[-1]:
   if i-m:a+=1;q.pop()
   else:print(a);break
  i=(i+1)%n