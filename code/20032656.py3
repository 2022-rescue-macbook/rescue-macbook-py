def rotate(l, n):
    return l[n:] + l[:n]


def turn(c, d):
    if c[0] == max(c):
        return c, d
    else:
        return rotate(c, c.index(max(c))), rotate(d, c.index(max(c)))


n = int(input())
c = []
for i in range(n):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    f = c[b]  # 보류
    d = [0 for j in range(len(c))]
    d[b] = 1
    print_cnt = 0
    q=True
    while q:
        if c[0] == f and d[0] == 1 and c[0] >= max(c):
            print_cnt += 1
            print(print_cnt)
            q=False

        elif c[0] == max(c):
            del c[0], d[0]
            print_cnt += 1

        else:
            c, d = turn(c, d)





