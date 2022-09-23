import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    check = [0 for _ in range(N)]
    check[M] = 1
    cnt = 0
    while True:
        if queue[0] == max(queue):
            cnt += 1
            if check[0] != 1:
                queue.pop(0)
                check.pop(0)
            else:
                print(cnt)
                break
        else:
            queue.append(queue.pop(0))
            check.append(check.pop(0))