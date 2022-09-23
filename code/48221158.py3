for _ in range(0, int(input())):
    n, m = map(int, input().split())
    Q = list(map(int, input().split()))
    u = max(Q)
    while True:
        if u == Q[0]:
            del Q[0]
            if m == 0:
                break
            u = max(Q)
        else:
            Q.append(Q[0])
            del Q[0]
            if m == 0:
                m = len(Q)
        m -= 1
    print(n-len(Q))