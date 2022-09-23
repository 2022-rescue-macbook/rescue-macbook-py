T = int(input())

for _ in range(T):

    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    current_position = M
    priority = queue[M]
    count = 0

    while len(queue) != 0:
        highest = max(queue)
        front = queue.pop(0)

        if current_position == 0:
            if priority == highest:
                count += 1
                break
            else:
                queue.append(front)
                current_position = len(queue) - 1
        else:
            current_position -= 1

            if front == highest:
                count += 1
            else:
                queue.append(front)

    print(count)