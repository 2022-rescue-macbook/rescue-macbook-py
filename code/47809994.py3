T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    m = max(arr)
    i = j = I = 0
    R = True
    n = 1
    while R:
        for j in range(N):
            k = (i+j) % N
            if arr[k] == m:
                if k == M:
                    print(n)
                    R = False
                else:
                    n += 1
                    I = k
        i = I
        m -= 1