import sys

result = []
T = int(sys.stdin.readline())
for i in range(T):
    cnt = 0
    N, M = map(int, sys.stdin.readline().split())
    printList = []
    checkList = [0 for _ in range(N)]
    checkList[M] = 1
    printList = list(map(int, sys.stdin.readline().split()))
    while True:
        if printList[0] == max(printList):
            cnt += 1
            if checkList[0] == 1:
                result.append(cnt)
                break
            else:
                del(printList[0])
                del(checkList[0])

        else:
            printList.append(printList[0])
            checkList.append(checkList[0])
            del(printList[0])
            del(checkList[0])

for i in result:
    print(i)