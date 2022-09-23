def sol():
    cnt=0
    while True:
        if arr[0] == max(arr):
            cnt+=1
            if idx[0] == 'target':
                break
            else:
                idx.pop(0)
                arr.pop(0)
        else:
            idx.append(idx.pop(0))
            arr.append(arr.pop(0))
    return cnt
Q = int(input())
for _ in range(Q):
    N, M=map(int, input().split())
    arr = list(map(int, input().split()))
    idx = list(range(len(arr)))
    idx[M] = 'target'
    print(sol())
