import sys;iN=lambda:map(int,sys.stdin.readline().split())
for _ in range(*iN()):
 N,M=iN();p=list(iN());q=sorted(p);o=1;i=0
 while 1:
  if p[i]==q[-1]:
   if i-M:o+=1;q.pop()
   else:print(o);break
  i=(i+1)%N