num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    target = m
    first = max(arr)
    cnt = 0
    while True:
        if arr[0] == first:
            cnt += 1
            if target == 0:
                print(cnt)
                break
            else:
                arr.pop(0)
                target -= 1
                first = max(arr)
        else:
            arr.append(arr.pop(0))
            if target == 0:
                target = len(arr) - 1
            else:
                target -= 1