from sys import stdin as st
def nQ(a,b,c):
    ks=iter(sorted(list(set(b)),reverse=True))
    oQ,curI,lastI,frstI=0,0,-1,0
    while True:
        if frstI==curI:
            curK=next(ks)
            curI=(lastI+1)%c
            frstI=curI
        if b[curI]==curK:
            oQ+=1
            lastI=curI
            if curI==a:
                return oQ
        curI+=1
        curI%=c
caseN=int(st.readline())
for i in range(caseN):
    N, Loc=map(int,st.readline().split())
    que=list(map(int,st.readline().split()))
    print(nQ(Loc,que,N))