import sys
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    idx = [0] * len(p)
    idx[m] = 1
    count = 0
    while 1:
        if p[0] == max(p):
            count += 1
            del p[0]
            if idx[0] == 1:
                print(count)
                break
            else: del idx[0]
        else:
            p.append(p.pop(0))
            idx.append(idx.pop(0))