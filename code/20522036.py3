import sys

s = sys.stdin.readline()
tc = int(s)

for t in range(tc):
    s = sys.stdin.readline()
    N,M = map(int,s.split())
    order = [i for i in range(N)]
    s = sys.stdin.readline()
    priority = list(map(int,s.split()))
    pq = []
    for i in range(N):
        pq.append((order[i],priority[i]))

    result = 1
    while True:
        flag = True
        p = pq[0][1]
        for i in range(1,len(pq)):
            if pq[i][1] > p:
                flag = False
                break

        if flag == True:
            if pq[0][0] == M:
                print(result)
                break
            else:
                pq.pop(0)
                result+=1
        else:
            pq.append(pq[0])
            pq.pop(0)



