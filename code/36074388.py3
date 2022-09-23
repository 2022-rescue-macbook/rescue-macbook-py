import sys

def is_top(arr:list,ele:int):
    for num in arr:
        if num > ele:
            return 0
    else:
        return 1


count = int(sys.stdin.readline())
for _ in range(count):
    n,m = map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))
    count = 0
    idx = m
    while True:
        if idx == 0 and is_top(arr,arr[0]):
            print(count+1)
            break
        elif is_top(arr,arr[0]):
            count += 1
            arr.pop(0)
            idx = (idx-1)%len(arr)
        else:
            arr.append(arr.pop(0))
            idx = (idx-1)%len(arr)