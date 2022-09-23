import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    target, arr[M] = arr[M], 0
    cnt = 1
    for x in range(9, target, -1):
        idx = -1
        for i, v in enumerate(arr):
            if v == x:
                idx = i
                cnt += 1
        if idx != -1 : arr = arr[idx+1:] + arr[:idx+1]
    for c in arr:
        if c == target: cnt += 1
        elif c == 0:
            print(cnt)
            break