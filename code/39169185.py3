import sys

# sys.stdin.readline().rstrip()
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    l = list()
    cnt = 0
    for i in sys.stdin.readline().split():
        l.append(i)
    remain = list(reversed(sorted(l)))
    p = 0
    length = len(l)
    importance = remain.pop(0)
    while True:
        if importance == l[p]:
            cnt += 1
            if p < m:
                m -= 1
            elif p == m:
                print(cnt)
                break
            l.pop(p)
            length -= 1
            importance = remain.pop(0)
        else:
            p += 1
        if p == length:
            p = 0
