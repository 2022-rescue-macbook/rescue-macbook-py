import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n,m = map(int,input().split())
    queue = list(map(int,input().split()))
    goalqueue = [0] * n
    goalqueue[m] = 1
    cnt = 0
    for i in range(n):
        while queue[0] != max(queue):
            queue.append(queue.pop(0))
            goalqueue.append(goalqueue.pop(0))
        cnt += 1
        queue.pop(0)
        if 1 == goalqueue.pop(0):
            break
    print(cnt)