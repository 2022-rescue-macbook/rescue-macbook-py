import sys

t = int(sys.stdin.readline().replace('\n', ''))
answer = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().replace('\n', '').split())
    numbers = list(map(int, sys.stdin.readline().replace('\n', '').split()))
    queue = []
    for a, b in zip(numbers, list(range(len(numbers)))):
        queue.append((a, b))
    priority = list(sorted(queue))
    goal = queue[m]
    result = 1
    while True:
        item = queue[0]
        del queue[0]
        if item[0] == goal[0] and item[1] == goal[1] and item[0] == priority[-1][0]:
            break
        if item[0] == priority[-1][0]:
            del priority[-1]
            result += 1
        else:
            queue.append(item)
    answer.append(str(result))
print('\n'.join(answer))
