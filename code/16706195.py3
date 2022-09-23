t=int(input())
for i in range(t):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    aa=[]
    for i in range(n):
        aa.append([i,a[i]])
    p=[]

    while a:
        if aa[0][1]==max(a):
            p.append(aa[0])
            aa.pop(0)
            a.remove(max(a))
        else:
            aa.append(aa[0])
            aa.pop(0)

    for i in p:
        if i[0]==m:
            print(p.index(i)+1)