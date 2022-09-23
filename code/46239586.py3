import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    idx = list(range(len(importance)))
    idx[M] = 'target'
    A = 0

    while True:
        if importance[0] == max(importance):
            A += 1
            if idx[0] == 'target':
                print(A)
                break
            else:
                importance.pop(0)
                idx.pop(0)
        else:
            importance.append(importance.pop(0))
            idx.append(idx.pop(0))