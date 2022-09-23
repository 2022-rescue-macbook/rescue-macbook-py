import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N,M=map(int,input().split())
    l=[*map(int,input().split())]
    d=c=b=0;k=max(l);v=l[M]
    c+=l.count(v)
    for j in range(M+1):
        if l[j]==v:b+=1
    while k!=v:
        n=0
        while (e:=l.pop(0)):
            if v==e:n+=1
            if e==k:k=max(l);break
            l.append(e)
        if n>=b:b=c-n+b
        else:b=b-n
        d+=1
    print(d+b)