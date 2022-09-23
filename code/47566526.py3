import sys

T = int(input())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    important = list(map(int, sys.stdin.readline().split()))
    order = list(range(len(important)))
    cnt = 0

    while True:
        value = important.pop(0)
        num = order.pop(0)

        if not important:
            cnt += 1
            break

        elif value < max(important):
            important.append(value)
            order.append(num)

        else:
            cnt += 1
            if num == M:
                break

    print(cnt)