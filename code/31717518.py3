import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m, k = map(int, input().split())
    L = list(map(int, input().split()))
    cnt = 0
    while True:
        B = True
        for i in L:
            if L[0] < i:
                k = (k-1)%len(L)
                L.append(L[0])
                L.pop(0)
                B = False
        if B:
            cnt += 1
            if k == 0:
                print(cnt)
                break
            else:
                L.pop(0)
                k -= 1