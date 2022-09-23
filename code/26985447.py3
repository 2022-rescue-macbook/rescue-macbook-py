for _ in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cache = [0]*N
    cache[M] = 1
    cnt = 0
    while True:
        if arr[0] == max(arr):
            cnt += 1
            if cache[0] == 1:
                print(cnt)
                break
            else:
                del arr[0]
                del cache[0]
        else:
            arr.append(arr[0])
            del arr[0]
            cache.append(cache[0])
            del cache[0]
