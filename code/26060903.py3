import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = [i for i in range(N)]
    cnt = 0
    while len(arr)>0:
        i = arr.pop(0)
        j = idx.pop(0)
        if len(arr)>0 and i<max(arr):
            arr.append(i)
            idx.append(j)
        else:
            cnt += 1
            if j==M:
                break
    print(cnt)