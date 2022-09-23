for _ in range(int(input())):
    N,M = map(int,input().split())
    Ns = list(map(int,input().split()))
    s,e = 0,N-1
    i = 0
    visit = [0]*N
    s2 = 0
    Ns2 = Ns[:]
    Ns2.sort()
    Ns2 = Ns2[::-1]
    while(s != e):
        if(Ns[s] != Ns2[s2]):
            e = (e+1)%N
            Ns[e] = Ns[s]
            s = (s+1)%N  
            i = (i+1)%N
            while(visit[i]):
                i = (i+1)%N
        else:
            if i == M:
                break
            s= (s+1)%N
            s2 = s2+1
            visit[i] = 1
            while(visit[i]):
                i = (i+1)%N
    print(s2+1)