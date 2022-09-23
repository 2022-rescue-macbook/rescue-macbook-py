a=int(input())
for i in range(a):
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=['x']*b[0]
    d[b[1]]='y'
    for j in range(b[0]):
        mnum=max(c)
        while not c[0]==mnum:
            c.append(c[0])
            del c[0]
            d.append(d[0])
            del d[0]
        if d[0]=='y':
            print(j+1)
            break
        else:
            del c[0]
            del d[0]