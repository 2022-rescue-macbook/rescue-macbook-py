import sys
input=sys.stdin.readline
#sys.setrecursionlimit(1000000)
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    L1=list(map(int,input().split()))
    L2=[i for i in range(n)]
    count=0
    while True:
        for i in range(0,L1.index(max(L1))):
            L1.append(L1.pop(0))
            L2.append(L2.pop(0))
        L1.pop(0)
        count+=1
        if L2.pop(0)==m:
            print(count)
            break