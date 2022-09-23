T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sorted(arr, reverse=True)

    j = 0
    c = 0
    for i in range(n):
        while arr[j] != s[i]:
            j += 1
            if j >= n:
                j = 0
        c += 1
        if j == m:
            break
        j += 1
        if j >= n:
            j = 0
    print(c)
