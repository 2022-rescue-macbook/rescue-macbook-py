import sys
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    List = list(map(int, sys.stdin.readline().split()))
    queue = [(List[i], i) for i in range(N)]
    MAX = max(List)
    count = 1
    while queue:
        if queue[0][0] < MAX:
            queue.append(queue.pop(0))
        else:
            temp = queue.pop(0)
            if queue:
                MAX = max([i[0] for i in queue])
            if temp[1] == M:
                print(count)
                break
            else:
                count += 1