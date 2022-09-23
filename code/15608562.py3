import sys

T = int(sys.stdin.readline())
while T:
    N, idx = map(int, sys.stdin.readline().split(' '))
    q = list(map(int, sys.stdin.readline().split(' ')))
    c = 1
    while q:
        if q[0] != max(q):
            q.append(q[0])
            del q[0]
            idx -= 1
        elif q[0] == max(q) and idx == 0:
            print(c)
            c += 1
            break
        elif q[0] == max(q):
            del q[0]
            idx -= 1
            c += 1
        if idx == -1: idx = len(q) - 1
    T -= 1