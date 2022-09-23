import sys

TestCase = int(sys.stdin.readline())
for i in range(TestCase):
    N,M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    arr_with_order = []

    for j in range(len(arr)):
        arr_with_order.append([arr[j], j])
        
    count = 0
    while True:
        if arr[0]==max(arr):
            if arr_with_order[0][1]==M:
                count+=1
                break
            arr.pop(0)
            arr_with_order.pop(0)
            count+=1
        else:
            arr.append(arr.pop(0))
            arr_with_order.append(arr_with_order.pop(0))
    print(count)