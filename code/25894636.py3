from sys import stdin 

testNum = int(stdin.readline())
for _ in range(testNum):
    count = 0
    N,M = map(int,stdin.readline().split())
    importance= list(map(int,stdin.readline().split()))
    idx = list(range(len(importance)))
    idx[M] = 'target'
    target = importance[M]
    while importance : 
        maxImp = max(importance)
        nodeImp = importance.pop(0)
        nodeIdx = idx.pop(0)
        if nodeImp == maxImp :
            count += 1
            if nodeIdx == 'target':
                print(count) 
                break
        else : 
            importance.append(nodeImp)
            idx.append(nodeIdx)