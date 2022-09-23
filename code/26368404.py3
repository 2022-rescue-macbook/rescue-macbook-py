n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    lst = [0 for i in range(N)]
    lst[M] = 1

    num = 0
    while True:
        if queue[0] == max(queue):
            num += 1
            if lst[0] == 1:
                print(num)
                break
            else:
                del queue[0]
                del lst[0]
        else:
            lst.append(lst[0])
            del lst[0]
            queue.append(queue[0])
            del queue[0]