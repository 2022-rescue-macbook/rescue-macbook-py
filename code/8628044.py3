x = lambda:map(int,input().split())
T = int(input())
for t in range(T):
    N,M = x()
    l = list(x())
    loc = -1
    cnt = 1
    for a in sorted(l,reverse=True):
        ls = l[loc+1:]+l[:loc+1]
        loc =  (loc+ls.index(a)+1)%len(l)
        if loc==M:
            break
        else:
            cnt+=1
    print(cnt)