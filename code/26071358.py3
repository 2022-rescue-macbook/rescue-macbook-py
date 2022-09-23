import sys
sys.setrecursionlimit(10**8)
T = int(input())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    que = list(map(int, sys.stdin.readline().split()))
    ans = 0
    idx = 0
    target = m
    while True:
        for i in range(idx+1, len(que)):
            if que[i] > que[idx]:
                que.append(que[idx])
                if idx == target:
                    target = len(que) - 1
                idx += 1
                break
        else:
            ans += 1
            if idx == target:
                print(ans)
                break
            idx += 1
            