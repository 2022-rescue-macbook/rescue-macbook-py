import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sol = 1
    N, M = map(int, input().split())
    importance = [int(w) for w in input().split()]
    queue = list(range(N))
    front = 0
    while len(queue) > front:
        target = queue[front]
        maximp = max(importance)
        if importance[target] < maximp:
            queue.append(target)
        elif target == M:
            break
        else:
            sol += 1
            importance[target] = 0
        front += 1
    print(sol)