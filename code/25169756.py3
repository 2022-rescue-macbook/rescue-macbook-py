import sys


input = sys.stdin.readline
case = int(input())
for _ in range(case):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    x = 0
    while True:
        if queue[0] == max(queue):
            queue.pop(0)
            if M == 0:
                x += 1
                print(x)
                break
            else:
                M -= 1
                x += 1
        else:
            queue.append(queue.pop(0))
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1