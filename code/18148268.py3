for i in ' '*int(input()):
    n,m=map(int,input().split())
    L=list(map(int,input().split()))
    ct=0
    q=[]
    for j in L:
        q.append((j,ct))
        ct+=1
    c=0
    while True:
        k=q.pop(0)
        mL=max(L)
        if k[0]==mL:
            c+=1
            if k[1]==m:break
            L.remove(k[0])
        else:
            q.append(k)
    print(c)