import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    Q=list(map(int,input().split()))
    cnt=0
    while True:
        #우선순위 젤 높으면 pop
        if Q[0]>=max(Q):
            Q.pop(0)
            cnt+=1
            if M==0:
                print(cnt)
                break
            else:
                M-=1
        else:
            tmp=Q.pop(0)
            Q.append(tmp)
            if M==0:
                M=len(Q)-1
            else:
                M-=1
