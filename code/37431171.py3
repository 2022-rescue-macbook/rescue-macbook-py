import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    checkList = [0 for _ in range(N)]
    checkList[M] = 1
    cnt = 0
    while True:
        if priority[0] == max(priority):
            cnt += 1
            if checkList[0] == 1:
                print(cnt)
                break
        else:
            priority.append(priority[0])
            checkList.append(checkList[0])
        del priority[0]
        del checkList[0]
