t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    v = list(map(int, input().split()))

    s = sorted(v, reverse=True)
    r = 0

    while True:
        k = v[0]
        del v[0]
        m -= 1

        if k == s[0]:
            r += 1
            del s[0]
            n -= 1

            if m < 0: break
        else:
            v.append(k)
            if m < 0: m = n - 1

    print(r)