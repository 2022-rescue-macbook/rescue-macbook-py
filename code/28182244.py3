T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    arr = [(idx, a) for idx, a in enumerate(arr)]
    count = 0
    max_a = max(arr, key = lambda x: x[1])[1]
    while count < N:
        if max_a == arr[0][1]:
            count += 1
            if arr[0][0] == M:
                print(count)
                break
            arr.pop(0)
            max_a = max(arr, key = lambda x: x[1])[1]
        else:
            arr.append(arr.pop(0))
