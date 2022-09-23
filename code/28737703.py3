from sys import stdin

t = int(input())
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    d = list(map(int, stdin.readline().split()))
    idx = m
    c = 0
    while True:
        x = max(d)
        if d[0] == x:
            d.pop(0)
            c += 1
            idx -=1
            if idx == -1:
                break
        else:
            d.append(d.pop(0))
            idx -= 1
            if idx < 0:
                idx = len(d) - 1
    print(c)