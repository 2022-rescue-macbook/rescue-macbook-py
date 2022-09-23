
def printOrder(docs, pos):
    printNum = 0

    while len(docs) > 0:
        curDoc = docs.pop(0)

        canPrint = True
        for doc in docs:
            if curDoc[1] < doc[1]:
                docs.append(curDoc)
                canPrint = False
                break

        if canPrint:
            printNum += 1
            if curDoc[0] == pos:
                print(printNum)
                break


t = int(input())

for _ in range(t):
    n, m = [int(i) for i in input().split(' ')]

    docs = []

    for value in input().split(' '):
        docs.append((len(docs), int(value)))

    printOrder(docs, m)
