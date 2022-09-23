n = int(input())
import sys
for _ in range(n):
    total, idx = list(map(int, sys.stdin.readline().strip().split()))
    li = list(map(int, sys.stdin.readline().strip().split()))
    queue = [(v, i) for i, v in enumerate(li)]
    answer = 0
    flag = False
    li.sort()
    while not flag:
        max_ = li[-1]
        while queue[0][0] < max_:
            queue = queue[1:] + queue[:1]
        if queue[0][1] == idx:
            answer += 1
            flag = True
            break
        queue.pop(0)
        li.pop()
        answer += 1
    print(answer)