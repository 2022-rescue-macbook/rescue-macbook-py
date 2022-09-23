N = int(input())

for _ in range(N):
    _, want = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    count = 0
    
    while True:
        if len(arr) > 1:
            head = arr[0]
            if head < max(arr):
                if want <= 0:
                    want = len(arr)-1
                else:
                    want -= 1
                arr.append(arr.pop(0))
            else:
                count += 1
                if want <= 0:
                    print(count)
                    break
                else:
                	want -= 1
                arr.pop(0)
        elif len(arr) == 1:
            count += 1
            if want <= 0:
                print(count)
                break
            else:
            	want -= 1
            arr.pop(0)
        else:
            break