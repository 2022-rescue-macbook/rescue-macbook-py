import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[M] = 'want'
    order = 0
    while True:
        if imp[0] == max(imp):
            order += 1
            if idx[0] == 'want':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
