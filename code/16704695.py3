import sys

n = int(sys.stdin.readline().strip())


for i in range(n):
    count = 0

    a, b = map(int, sys.stdin.readline().strip().split())
    queue = list(map(int, sys.stdin.readline().strip().split()))

    while bool(queue):
        if b == 0:
            if queue[0] >= max(queue):
                del queue[0]
                count += 1
                break
            else:
                queue.append(queue.pop(0))
                b = len(queue) - 1
        else:
            if queue[0] >= max(queue):
                del queue[0]
                count += 1
                b -= 1
            else:
                queue.append(queue.pop(0))
                b -= 1

    print(count)
