#1966 프린터 큐

import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n,m=map(int,sys.stdin.readline().split())
    imp=list(map(int,sys.stdin.readline().split()))
    ans=0
    while imp:
        if max(imp)==imp[0]:
            del imp[0]
            ans+=1
            if m==0:
                break
        else:
            imp.append(imp[0])
            del imp[0]
        m-=1
        if m==-1:
            m+=len(imp)
    print(ans)