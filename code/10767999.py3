n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    q = []
    q = list(map(int, input().split()))
    sorted_q = q.copy()
    sorted_q.sort(reverse=True)

    ans = 0
    idx = m
    while q:
        if q[0] == sorted_q[0]:
            sorted_q.pop(0)
            q.pop(0)
            ans += 1
            if idx == 0:
                break
            idx -= 1
        else:
            b = q.pop(0)
            q.append(b)
            idx -= 1
            if idx < 0:
                idx = len(q) - 1
    print(ans)

        