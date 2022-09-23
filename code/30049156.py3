T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = input().split()

    queue = []
    value = sorted(arr, reverse=True)

    for i in range(N):
        queue.append([i, arr[i]])

    i = 0
    cnt = 1
    while True:
        index, num = queue.pop(0)
        if num == value[i]:
            if index == M:
                break
            i += 1
            cnt += 1
        else:
            queue.append([index, num])

    print(cnt)