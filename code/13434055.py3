f=lambda:map(int,input().split())
for i in range(int(input())):
    n,m=f()
    k,a=1,[(i,0) for i in f()]
    a[m] = (a[m][0],1)
    while True:
        if max(a)[0] > a[0][0]:
            a+=a[0],
        else:
            if a[0][1]>0:
                print(k)
                break
            k+=1
        a.pop(0)