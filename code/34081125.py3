n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 1
    t2 = [0]*a
    t2[b] = 1
    while True:
        c = t[0]
        d = t2[0]
        if c == max(t):
            if d == 1:
                break
            else:
                ans += 1
        else:
            t.append(c)
            t2.append(d)
        c = t.pop(0)
        d = t2.pop(0)
    print(ans)