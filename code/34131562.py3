times = int(input())
for case in range(times):
    numberOfDocuments, quest = input().split()
    numberOfDocuments = int(numberOfDocuments)
    quest = int(quest)
    queue = [int(x) for x in input().split()]
    
    first = 0
    order = -1
    
    while True:
        maxNum = max(queue)
        if maxNum < 0:
            break
        idx = first
        for i in queue:
            if queue[idx] == maxNum:
                queue[idx] = order
                order = order - 1
                first = (idx + 1) % numberOfDocuments
            idx = (idx + 1) % numberOfDocuments
    
    print(queue[quest] * -1)