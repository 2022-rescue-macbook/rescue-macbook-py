import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    g = list(map(int,input().split()))
    l = [index for index,value in enumerate(g)]
    result = 1
    while g:
        v = g[0]
        vv = l[0]
        if v >= max(g):
            if vv == y:
                print(result)
                break
            else:
                result += 1
                g.pop(0)
                l.pop(0)
        else:
            g.append(g.pop(0))
            l.append(l.pop(0))