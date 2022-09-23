from sys import stdin

T = int(stdin.readline())
for tc in range(T):
    N, M = map(int, stdin.readline().split())
    Imp = list(map(int, stdin.readline().split()))
    que = [[i, Imp[i]] for i in range(N)]
    N = [Imp.count(i) for i in range(1, 10)]
    n, cnt, ans = 8, 0, -1
    while n >= 0:
        while N[n] == 0:
            n -= 1
        if que[0][1] == n+1:
            N[n] -= 1
            cnt += 1
            if que[0][0] == M:
                ans = cnt
                break
            que.pop(0)
        else:
            que.append(que.pop(0))
    print(ans)