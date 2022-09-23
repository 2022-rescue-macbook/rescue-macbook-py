import sys
T = int(sys.stdin.readline())
Queue = []
where = []
loop = 1
for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    Queue = list(map(int, sys.stdin.readline().split()))
    while Queue:
            wh = Queue.index(max(Queue))
            where.append(wh)
            Queue = Queue[wh + 1::] + Queue[0:wh:1]
            if W == wh:
                print(loop)
                break
            loop += 1
            if wh > W:
                W = N - loop + 1 - (wh - W)
            else:
                W = (W - wh) - 1
    where = []
    Queue = []
    loop = 1