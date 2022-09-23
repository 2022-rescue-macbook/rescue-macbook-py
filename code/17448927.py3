from collections import deque
from sys import stdin

count = int(input())
while count:
    n, index = map(int, stdin.readline().split())
    documents = list(map(int, stdin.readline().split()))
    marked = deque([(v, True) if i == index else (v, False) for i, v in enumerate(documents)])
    priorities = sorted(documents)
    max_p = priorities[-1]
    printed = 1
    while True:
        if marked[0][0] == max_p:
            d = marked.popleft()
            if d[1]:
                print(printed)
                break
            else:
                printed += 1
                priorities.pop()
                max_p = priorities[-1]
        else:
            marked.rotate(-1)
    count -= 1