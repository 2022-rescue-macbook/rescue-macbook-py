import sys
input=sys.stdin.readline

T=int(input())
for i in range(T) :
    N, M=map(int, input().split())
    Q=list(map(int, input().split()))
    idx=[0]*N
    idx[M]=1
    count=0
    while True :
        if Q[0]==max(Q) :
            count+=1
            if idx[0]==1 :
                print(count)
                break
            else :
                Q.pop(0)
                idx.pop(0)
        else :
            Q.append(Q.pop(0))
            idx.append(idx.pop(0))