T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    Priority = list(map(int, input().split()))
    Queue = []
    for i in range(N):
        Queue.append(i)
    o = 0
    while (True):
        if (Priority[0] == max(Priority)):
            Priority.pop(0)
            o += 1
            if (Queue.pop(0) == M):
                print(o)
                break
        else:
            Priority.append(Priority.pop(0))
            Queue.append(Queue.pop(0))
