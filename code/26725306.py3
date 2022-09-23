import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int, sys.stdin.readline().split())
    que = list(map(int, sys.stdin.readline().split()))

    result = 0
    while True:
        M -= 1
        maximum = max(que)
        temp = que.pop(0)
        if temp != maximum: 
            que.append(temp)
            if M == -1: 
                M = len(que)-1
        else: 
            result += 1
            if M == -1: 
                print(result)
                break