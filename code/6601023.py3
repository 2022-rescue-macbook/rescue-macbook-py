for _ in 'a'*int(input()):
    N,M=map(int,input().split())
    Qp=list(map(int,input().split()));c=max(Qp)
    Qd=[i for i in range(N)]
    t=1
    while True:
        if Qp[0] < c:
            Qp.append(Qp.pop(0))
            Qd.append(Qd.pop(0))
        else:
            Qp.pop(0);
            v=Qd.pop(0)
            if v == M:
                print(t)
                break
            t+=1
            c=max(Qp)