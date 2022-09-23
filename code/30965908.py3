import sys
def r():return list(map(int,sys.stdin.readline().split()))
for i in range(int(input())):
  n,d=r();st=0;end=n;re=[]
  a=r();b=sorted(a);a=list(zip(a,range(n)))
  while end-st>0:
    t=b.pop()
    while a[st][0]!=t:a.append(a[st]);st+=1;end+=1
    re.append(a[st][1]);st+=1
  print(re.index(d)+1)