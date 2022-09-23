from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
while T:
    N, M = map(int, input().rstrip().split())
    priority = list(map(int, input().rstrip().split()))
    q = deque()
    for i in range(N):
        q.appendleft((i, priority[i]))
    priority.sort(reverse=True)
    turn = 0
    while True:
        t = q.pop()
        if t[1] < priority[turn]:
            q.appendleft(t)
        else:
            if t[0] == M:
                print(turn+1)
                break
            turn += 1
    T-=1