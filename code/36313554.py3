import sys
T = int(input())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    value = list(arr)
    arr = list(enumerate(arr))
    cnt = 0
    while 1:
        if arr[0][1] == max(value):
            cnt += 1
            if arr[0][0] == M:
                print(cnt)
                break
            value.remove(arr[0][1])
            del arr[0]
        else:
            arr.append(arr.pop(0))