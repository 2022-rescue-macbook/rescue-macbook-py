import sys

tc=int(sys.stdin.readline())

for i in range(tc):
    a,b=map(int,sys.stdin.readline().split())
    li=list(map(int,sys.stdin.readline().split()))
    count=1
    
    for j in range(a):
        t=li.index(max(li))
        if t>b:
            b=(a-t)+b
        elif t<b:
            b=b-t
        elif t==b:
            break
        li=li[t:]+li[:t]
        li[0]=0
        count+=1
    print(count)