import sys

n = int(sys.stdin.readline())

for i in range(n):
    lng, idx = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    temp = [0 for i in range(lng)]
    temp[idx]=1
    cnt = 0
    
    while 1:
        if arr[0] == max(arr):
            cnt += 1
            if temp[0] == 1:
                print(cnt)
                break
            else:
                arr.pop(0)
                temp.pop(0)    
        else:
            arr.append(arr.pop(0))
            temp.append(temp.pop(0))