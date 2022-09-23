from collections import deque
import sys
read = sys.stdin.readline

t = int(read().strip())
for _ in range(t):
    n, m = map(int, read().strip().split())
    priority = list(map(int, read().strip().split()))
    max_prior = max(priority)

    q = deque()
    for i, p in enumerate(priority):
        q.append((i, p))

    cnt = 1

    while q:
        now, prior = q.popleft()
        if prior == max_prior:
            if now == m:
                print(cnt)
                break
            else:
                priority.remove(max_prior)
                max_prior = max(priority)
                cnt += 1
        else:
            q.append((now, prior))
