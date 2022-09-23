import sys

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc) :
    n, m = map(int, sys.stdin.readline().split())
    imp = list(map(int, sys.stdin.readline().split()))
    imp_idx = [0 for _ in range(n)]
    imp_idx[m] = 'target'
    cnt = 0

    while True :
        if imp[0] == max(imp) :
            cnt += 1
            if imp_idx[0] == 'target' :
                print(cnt)
                break
            else :
                del imp[0]
                del imp_idx[0]

        else :
            imp.append(imp[0])
            imp_idx.append(imp_idx[0])
            del imp[0]; del imp_idx[0]

