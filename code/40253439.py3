from sys import stdin
T = int(stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, stdin.readline().rstrip().split())
    Arr = list(map(int, stdin.readline().rstrip().split()))
    cnt = list(Arr.count(x) for x in range(0, 10))
    start = 0
    Flag = False
    c = 0
    for p in range(9, 0, -1):
        while cnt[p] and not Flag:
            if p in Arr[start:]:
                start = Arr[start:].index(p) + start
                c += 1
                cnt[p] -= 1
                if start == M:
                    Flag = True
                    print(c)
                start += 1
            else: start = 0
        if Flag: break
