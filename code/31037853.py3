N = int(input())
prtList = [0] * N

for i in range(N) :
    length, searchIndex = map(int, input().split(" "))
    l = list(map(int, input().split(" ")))
    sortList = []
    for j in range(length) :
        sortList.append(l[j])
    l.sort()
    startIndex = 0
    while True :
        if startIndex >= len(sortList) :
            startIndex = 0
        if sortList[startIndex] == l[len(l)-1] :
            prtList[i] += 1
            if startIndex == searchIndex :
                break
            del l[len(l)-1]
        startIndex += 1

for i in prtList:
    print(i)