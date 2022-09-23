# 1966 - 프린터 큐

def getOrder(paper, userLoc, userList):
    location = userLoc
    importancy = userList
    index = 0
    order = 1

    while True:
        if max(importancy) != importancy[index]:
            poped = importancy.pop(0)
            importancy.append(poped)
            if location > 0:
                location -= 1
            else:
                location = len(importancy)-1
        else:
            # 출력
            if index == location:
                return order
            else:
                importancy.pop(0)
                location -= 1
                order += 1


tastCase = int(input())
result = []

for t in range(tastCase):
    paper, userLoc = map(int, input().split())
    userList = list(map(int, input().split()))
    result.append(getOrder(paper, userLoc, userList))

for i in range(tastCase):
    print(result[i])
