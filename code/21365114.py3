T = int(input())
for _ in range(T):
    n, p = map(int,input().split())
    l = list(map(int,input().split()))
    key = l[p]
    l.insert(p+1,-1)
    ans = 0
    while 1:
        #print(l)
        M = max(l)
        if key==M:
            i = l.index(M)
            if l[i+1]==-1: break
        else:
            i = 0
            while 1:
                if l[i]==M: break
                i+=1
        l = l[i+1:]+l[:i]
        ans += 1
    print(ans+1)