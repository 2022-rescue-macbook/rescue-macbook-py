import sys

N = int(sys.stdin.readline())

for i in range(N):
    count = 0
    a, b = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))

    while b != -1:
        if queue[0] == max(queue):
            del queue[0]
            b -= 1
            count += 1
        else:
            queue.append(queue[0])
            del queue[0]

            if b == 0:
                b = len(queue) - 1
            else:
                b -= 1

    print(count)