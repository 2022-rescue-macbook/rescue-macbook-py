import sys

def sortOrder(printOrder, importance):
    initList = printOrder
    orderedList = []

    while initList:
        for i in initList:
            if importance[initList[0]] < importance[i]:
                temp = initList.pop(0)
                initList.append(temp)
                break
            if len(initList) == 1 or i == initList[-1]:
                orderedList.append(initList.pop(0))
    return orderedList


case = int(sys.stdin.readline().strip())
for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    printOrder = [i for i in range(n)]
    orderedList = sortOrder(printOrder, importance)
    place = 1 + orderedList.index(m)
    print(place)