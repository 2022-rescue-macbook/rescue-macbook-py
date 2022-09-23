import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    N, check = map(int, input().split())
    M = list(map(int, input().split()))
    idx = list(range(len(M)))
    idx[check] = 'target'

    for j in range(N):
        while max(M) != M[0]:
            M.append(M.pop(0))
            idx.append(idx.pop(0))

        M.pop(0)
        if idx[0] == 'target':
            print(j + 1)
        idx.pop(0)