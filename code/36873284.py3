def get(): return map(int, input().split())
for _ in range(int(input())):
    N, M = get()
    q = list(get())
    while q:
        m = max(q)
        i = q.pop(0)
        if i == m:
            if M == 0:
                print(N-len(q))
                break
        else:
            q.append(i)
        M = (M-1) % len(q)