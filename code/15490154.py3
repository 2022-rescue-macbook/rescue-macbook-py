n = int(input())
for i in range(n):
    arr_size, index = map(int, input().split())
    queue = list(map(int, input().split()))
    check = [0 for j in range(arr_size)]
    check[index] = 'T'

    count = 0
    while 1:
        if queue[0] == max(queue):
            count+=1
            if check[0] == 'T':
                print(count)
                break
            else:
                queue.pop(0)
                check.pop(0)
        else:
            queue.append(queue.pop(0))
            check.append(check.pop(0))