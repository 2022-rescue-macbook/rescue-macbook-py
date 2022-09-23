import sys

tc = int(sys.stdin.readline())

for t in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    importants = list(map(int, sys.stdin.readline().split()))

    queue = []
    for i in range(n):
        queue.append([i])
        queue[i].append(importants[i])

    importants = sorted(importants)
    importants.reverse()

    cnt = 0
    while True:
        if importants[0] == queue[0][1]:
            cnt += 1
            if queue[0][0] == m:
                break
            queue.remove(queue[0])
            importants.remove(importants[0])
        else:
            queue.append(queue[0])
            queue.remove(queue[0])
    print(cnt)