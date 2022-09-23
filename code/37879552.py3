import sys
input = sys.stdin.readline
a = int(input())

for i in range(a):
    n, idx = map(int, input().split())
    priority = list(map(int,input().split()))

    checkList = [0 for _ in range(n)]
    checkList[idx] = "target"

    count = 0

    while True:
        if priority[0] == max(priority):
            count += 1

            if checkList[0] == 'target':
                print(count)
                break
        
            priority.pop(0)
            checkList.pop(0)
        else:
            priority.append(priority.pop(0))
            checkList.append(checkList.pop(0))
