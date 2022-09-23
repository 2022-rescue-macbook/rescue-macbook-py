T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    idx = [False] * N
    idx[M] = True
    count = 0

    while (True):
        if queue[0] == max(queue):
            count += 1
            if (idx[0] == True):
                print(count)
                break
            else :
                queue.pop(0)
                idx.pop(0)
        else :
            queue.append(queue.pop(0))
            idx.append(idx.pop(0)) 