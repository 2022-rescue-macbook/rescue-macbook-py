import sys

case_num = int(sys.stdin.readline())

for _ in range(case_num):
    N, M = map(int, (sys.stdin.readline().split()))
    priority = list(map(int, sys.stdin.readline().split()))
    idx = [False for _ in range(N)]
    idx[M] = True
    count = 0

    while True:
        if priority[0] != max(priority):
            priority.append(priority.pop(0))
            idx.append(idx.pop(0))
        else:
            if idx[0]:
                print(count+1)
                break
            else:
                count += 1
                priority.pop(0)
                idx.pop(0)
