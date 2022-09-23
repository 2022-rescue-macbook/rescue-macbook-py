import sys

T = int(input())
for _ in range(T):
    N, idx = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    i = 0
    while True:
        if idx == 0:
            if arr[0] != max(arr):
                arr.append(arr.pop(0))
                idx = len(arr) - 1
            else:
                i += 1
                break
        else:
            idx -= 1
            if arr[0] != max(arr):
                arr.append(arr.pop(0))
            else:
                arr.pop(0)
                i += 1
    print(i)