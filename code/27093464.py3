import sys
import heapq
t = int(sys.stdin.readline())
n = []
m = []
docu = []
num = []
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    n.append(a)
    m.append(b)
    docu.append([])
    num.append([])
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(a):
        docu[i].append([temp[j], j])
        heapq.heappush(num[i], (-temp[j], temp[j]))
for i in range(t):
    count = 0
    while docu[i]:
        node = docu[i].pop(0)
        if node[0] == num[i][0][1]:
            heapq.heappop(num[i])
            count += 1
            if node[1] == m[i]:
                print(count)
                break
        else:
            docu[i].append(node)
