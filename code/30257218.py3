def makeArr(N):

    arr = list(map(int, input().split()))
    return arr

def check(arr):
    cur = arr[0]

    for idx in range(1, len(arr)):
        if arr[idx] > cur:
            return False
    return True

T = int(input())

for _ in range(T):
    N, idx = map(int, input().split())
    arr = makeArr(N)
    cnt = 0

    while arr:
        if check(arr):
            arr.pop(0)
            cnt += 1
            idx -= 1

            if idx == -1:
                print(cnt)
                break
        else:
            arr.append(arr.pop(0))
            idx -= 1
            if idx == -1:
                idx = len(arr) - 1