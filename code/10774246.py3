def solve(n, m, queue) :
    qu = list(enumerate(queue))
    pr = sorted(queue, reverse = True)
    pi, qi = 0, 0
    while True :
        if qu[qi][1] < pr[pi] :
            qu.append(qu[qi])
            qi += 1
        elif qu[qi][0] == m :
            return pi+1
        else :
            qi += 1
            pi += 1

tc = int(input())
for t in range(tc) :
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    print(solve(n,m,q))
