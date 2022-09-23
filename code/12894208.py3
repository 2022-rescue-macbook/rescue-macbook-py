def printQueue(baseList, checkList):
    cnt = 0

    while True:
        if baseList[0] == max(baseList):
            if checkList[0] == 'T':
                cnt += 1
                print(cnt)
                break
            else:
                cnt += 1
                del baseList[0]
                del checkList[0]

        else:
            baseList.append(baseList[0])
            checkList.append(checkList[0])
            del baseList[0]
            del checkList[0]


a = int(input())

for _ in range(a):
    n, m = map(int, input().split(" "))
    baseList = list(map(int, input().split(" ")))
    checkList = [0 for _ in range(n)]
    checkList[m] = 'T'
    printQueue(baseList, checkList)
