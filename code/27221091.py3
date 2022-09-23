import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    num=list(map(int,input().split()))
    idx=[0 for _ in range(n)]
    idx[m]=1
    cnt=0
    while True:
        if num[0]==max(num):
            cnt+=1
            if idx[0]==1:
                print(cnt)
                break
            else:
                idx.pop(0)
                num.pop(0)
        else:
            idx.append(idx.pop(0))
            num.append(num.pop(0))