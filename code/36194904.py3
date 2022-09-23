T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    P=list(map(int,input().split()))
    Q=[]
    S=[]
    for j in range(N):
        Q.append([j,P[j]])
    P = sorted(P, reverse=True)
    while P!=[]:
        if Q[0][1]==P[0]:
            S.append(Q[0])
            Q.remove(Q[0])
            P.remove(P[0])
        else:
            Q.append(Q[0])
            Q.remove(Q[0])
    for j in range(len(S)):
        S[j]=[S[j][0],S[j][1],j]
    S = sorted(S)
    print(S[M][2]+1)