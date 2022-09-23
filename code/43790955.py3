import sys
read = sys.stdin.readline

t = int(read())
for _ in range(t):
    n, m = map(int, read().split())
    arr = list(map(int, read().split()))
    count = [0] * 10
    idx = 0
    for i in arr:
        count[i] += 1
    result = 0
    for i in reversed(range(arr[m] + 1, 10)):
        result += count[i]
        for j in range(1, n):
            if arr[idx-j] == i:
                idx = (idx-j) % n
                break
    if idx > m:
        idx -= n
    for i in range(idx, m):
        if arr[i] == arr[m]:
            result += 1
    result += 1
    print(result)
