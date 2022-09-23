for _ in range(int(input())):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    k = q[m]
    cs = [[] for _ in range(10)]
    for i, e in enumerate(q):
        cs[e].append(i)
    s, i = 1, -1
    for j in range(9, k, -1):
        l = cs[j]
        if l:
            s += len(l)
            cs[j] = [e for e in l if e > i] + [e for e in l if e < i]
            i = cs[j][-1]
    l = cs[k]
    cs[k] = [e for e in l if e > i] + [e for e in l if e < i]
    s += cs[k].index(m)
    print(s)