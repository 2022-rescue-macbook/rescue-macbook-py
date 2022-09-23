from sys import stdin
input = stdin.readline
Times = int(input())
def append(n, m, l):
    l.append(l.pop(0))
    if m == 0:
        m = len(l) - 1
    else:
        m -= 1
    return n, m, l
def remove(n, m, l):
    l.pop(0)
    m -= 1
    return n, m, l

for i in range(Times):
    n, m = map(int, input().split(' '))
    l = list(map(int, input().split(' ')))
    ans = 0
    while True:
        if l[0] == max(l):
            n, m, l = remove(n, m, l)
            ans += 1
        else:
            n, m, l = append(n, m, l)
        if m == -1:
            break
    print(ans)