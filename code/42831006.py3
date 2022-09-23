import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N, M=map(int, input().split())
    cost=list(map(int, input().split()))
    ch=[0]*N
    ch[M]=1
    ans=0
    while 1:
        if not cost[0]-max(cost):
            ans+=1
            if ch[0]-1:
                del cost[0]
                del ch[0]
            else:
                print(ans)
                break
        else:
            cost.append(cost[0])
            ch.append(ch[0])
            del cost[0]
            del ch[0]