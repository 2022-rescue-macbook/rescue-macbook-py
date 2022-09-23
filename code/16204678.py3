from collections import deque
from sys import stdin

T = int(stdin.readline())

for i in range(T):
    N, M = map(int, stdin.readline().split())
    q = deque()
    ans = []

    inputs = list(map(int, stdin.readline().split()))
    inputs_sorted = sorted(inputs, reverse=True)

    # print(inputs_sorted)

    for idx, i in enumerate(inputs):
        temp = [idx] + [i]
        q.append(temp)
    # print(q)

    cnt = 1
    for max_num in inputs_sorted:
        temp = []
        while(True):
            if max_num == q[0][1]:
                temp = q.popleft()
                ans.append(temp)
                break
            q.rotate(-1)

        if temp[0] == M:
            print(cnt)
            break

        cnt += 1
