T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    l = list(map(int, input().split()))
    l2 = []
    max_l = max(l)
    for i in range(len(l)):
        l2.append(i)
    cnt = 1
    while True:
        while max_l != l[0]:
            a = l.pop(0)
            l.append(a)
            b = l2.pop(0)
            l2.append(b)
        if l2.pop(0) == M:
            print(cnt)
            break
        else:
            cnt += 1
            l.pop(0)
            max_l = max(l)
            continue



