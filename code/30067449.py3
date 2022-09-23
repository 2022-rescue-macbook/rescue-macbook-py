import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    queue = list(map(int, input().split()))
    locat = [0]*n
    locat[m] = 1
    cnt = 0

    while True:
        if queue[0] == max(queue):
            cnt += 1
            if locat[0] == 1:
                print(cnt)
                break
            else:
                del queue[0]
                del locat[0]
        else:
            queue.append(queue[0])
            del queue[0]
            locat.append(locat[0])
            del locat[0]