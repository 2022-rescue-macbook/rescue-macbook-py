def rotate(L, N):
    return L[N:]+L[:N]

def check():
    global Q, Q_val
    if Q[0]==Q_val[-1]:
        return True
    else:
        return False

TC=int(input())
for _ in range(TC):
    N,M=map(int,input().split())
    Q=list(map(int,input().split()))
    Q_pos=[i for i in range(N)]
    Q_val=list(set(Q))
    Q_val=sorted(Q_val)
    target = Q.index(Q_val[-1])
    cnt=1
    now=Q_pos[0]
    while now!=M or Q[0]!=Q_val[-1]:
        if check():
            del Q[0], Q_pos[0]
            if Q_val[-1] not in Q:
                del Q_val[-1]
            cnt+=1
        else:
            target=Q.index(Q_val[-1])
            Q=rotate(Q, target)
            Q_pos=rotate(Q_pos, target)
        now = Q_pos[0]
    print(cnt)