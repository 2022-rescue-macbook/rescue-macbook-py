import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    idx = [0 for _ in range(n)]
    idx[m] = 1
    cnt = 0
    que = []
    while q:
        if q[0] == max(q):
            cnt += 1
            if idx[0] == 0:
                q.pop(0)
                idx.pop(0)
            else:
                break
        else:
            q.append(q.pop(0))
            idx.append(idx.pop(0))
    print(cnt)