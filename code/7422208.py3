import sys
read = sys.stdin.readline

tc = int(read())
for _ in range(tc):
    N, M = map(int, read().split())
    queue = list(map(int, read().split()))[::-1]
    M = N - M - 1
    squeue = sorted(queue)
    cnt = 0
    while len(queue) > 0:
        while queue[-1] != squeue[-1]:
            queue.insert(0, queue[-1])
            queue.pop()
            M = (M+1) % len(queue)
        if M == len(queue)-1:
            print(cnt+1)
            break
        queue.pop()
        squeue.pop()
        cnt += 1
