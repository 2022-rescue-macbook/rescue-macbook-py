import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    queue = list(map(int,input().split()))

    count = 0
    while True:
        if max(queue) > queue[0]:
            queue.append(queue.pop(0))
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1
        else:
            queue.pop(0)
            count += 1
            if m == 0:
                print(count)
                break
            else:
                m -= 1