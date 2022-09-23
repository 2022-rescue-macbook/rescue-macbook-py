T = int(input())

for i in range(T):

    N, D = map(int, input().split())
    arr = list(map(int, input().split()))

    target = [0]*N
    target[D] = 1


    cnt = 1
    while True:
        if arr[0] == max(arr):
            if target[0] == 1:
                print(cnt)
                break
            elif target[0] == 0:
                arr.pop(0)
                target.pop(0)
                cnt += 1
        else:
            arr.append(arr.pop(0))
            target.append(target.pop(0))