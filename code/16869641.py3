import sys

t = int(sys.stdin.readline())

for i in range(t):
    n,m = list(map(int, sys.stdin.readline().split(" ")))
    arr = list(map(int, sys.stdin.readline().split(" ")))
    queue = []
    for q in range(n):
        queue.append([q,arr[q]])
    x = 0
    while x < n:
        is_bigger = False
        for y in range(x,n):
            if queue[x][1] < queue[y][1]:
                is_bigger = True
                break
        if is_bigger:
            queue.append(queue.pop(x))
        else:
            x += 1
    for x in range(len(queue)):
        if queue[x][0] == m:
            print(x+1)