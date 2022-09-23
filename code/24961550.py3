m = int(input())

for i in range(m):
    n, t = map(int, input().split())
    l = list(map(int, input().split()))
    s = list(range(0, n))
    c = 1
    while True:
        if max(l) == l[0]:
            if s[0] == t:
                print(c)
                break
            c += 1
            s = s[1:]
            l = l[1:]
        else:
            s = s[1:] + [s[0]]
            l = l[1:] + [l[0]]