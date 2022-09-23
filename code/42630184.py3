import sys
input = sys.stdin.readline

def check_max():
    global max_n
    max_n = 0
    for i in range(len(arr)):
        if arr[i][1] > max_n:
            max_n = arr[i][1]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(enumerate(map(int, input().split())))
    cnt = 0
    max_n = 0
    
    check_max()
    while True:
        if arr[0][1] >= max_n:
            cnt += 1
            if arr[0][0] == M:
                break
            arr.pop(0)
            check_max()
        else:
            doc = arr.pop(0)
            arr.append(doc)

    print(cnt)