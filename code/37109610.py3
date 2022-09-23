import sys
input = sys.stdin.readline
def search(q, r, x, y):
    num = 1
    for i in r:
        try:
            s = q.index(i,s,x)
        except:
            s = q.index(i)
        if s == y:
            return num
        q.pop(s)
        if s < y:
            y -= 1
        num += 1
        x -= 1

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    p = list(map(int, input().split()))
    M = sorted(p, reverse = True)
    print(search(p, M, a, b))