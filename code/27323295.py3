test_case = int(input())
for t in range(test_case):
    n, location = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    while arr:
        if location == 0:
            if arr[location] == max(arr):
                cnt += 1
                print(cnt)
                break
            else:
                arr.append(arr.pop(0))
                location = len(arr) - 1

        else:
            if arr[0] == max(arr):
                arr.pop(0)
                cnt += 1
                location = location - 1
            else:
                arr.append(arr.pop(0))
                location = location - 1
            

