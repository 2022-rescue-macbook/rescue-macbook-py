T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    queue = [int(x) for x in input().split()]
    cnt = i = 0
    tmp = M

    while True:
        if queue[0] == max(queue):
            queue.pop(0)
            cnt += 1
            if tmp == 0:
                break
        else:
            queue.append(queue.pop(0))
        
        if tmp == 0:
            tmp = len(queue) - 1
        else:
            tmp -= 1
    
    print(cnt)